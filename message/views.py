from rest_framework import generics

from message.models import Message
from message.serializers import MessageSerializer


class MessageListView(generics.ListAPIView):
    queryset = Message
    serializer_class = MessageSerializer
