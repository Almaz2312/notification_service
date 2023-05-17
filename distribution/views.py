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
        send_message.apply_async([data], eta=data['sending_datetime'])
        return instance


class DistributionDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distribute.objects.all()
    serializer_class = DistributeSerializer

    def perform_update(self, serializer):
        instance_id = serializer.date.get('id')
        instance = Distribute.objects.get(id=instance_id)
        task_id = instance.task_id
        task = send_message.AsyncResult(task_id)
        task.eta = serializer.data.get("sending_datetime")
        task.save()
        return instance
