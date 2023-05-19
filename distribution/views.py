from rest_framework import generics

from distribution.models import Distribute
from client.models import Client
from distribution.serializers import DistributeSerializer
from distribution.tasks import send_message


class DistributionListCreateView(generics.ListCreateAPIView):
    queryset = Distribute.objects.all()
    serializer_class = DistributeSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        data = serializer.data
        check = Client.objects.filter(tag=None, code=None)
        if not check:
            print('Empty!!!')
        print(check)
        print(data)
        send_message([data])
        return instance


class DistributionDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distribute.objects.all()
    serializer_class = DistributeSerializer

    # def perform_update(self, serializer):
    #     self.update(serializer)
    #
    #     instance_id = serializer.data.get('id')
    #     instance = Distribute.objects.get(id=instance_id)
    #     task_id = instance.task_id
    #     task = send_message.AsyncResult(task_id)
    #     task.eta = serializer.data.get("sending_datetime")
    #     task.save()
    #     return instance
    #
    # def partial_update(self, request, *args, **kwargs):
    #     self.partial_update(request, *args, **kwargs)
    #
    #     instance = self.get_object()
    #     task_id = instance.task_id
    #     task = send_message.AsyncResult(task_id)
    #     task.eta = instance.sending_datetime
    #     task.save()
    #     return instance
