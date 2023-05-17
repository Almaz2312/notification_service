from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from message.models import Message
from message.serializers import MessageSerializer


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["distribution", "status"]