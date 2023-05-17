from rest_framework import generics

from distribution.models import Distribute
from distribution.serializers import DistributeSerializer
from distribution.tasks import send_message


class DistributionListCreateView(generics.ListCreateAPIView):
    queryset = Distribute.objects.all()
    serializer_class = DistributeSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_message.apply_async(instance, eta=serializer.data.get('sending_datetime'))
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
