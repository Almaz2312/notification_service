from rest_framework import generics

from client.models import Operator, Client
from client.serializers import OperatorSerializer, ClientSerializer


class OperatorListCreateView(generics.ListCreateAPIView):
    queryset = Operator
    serializer_class = OperatorSerializer


class OperatorDetailDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Operator
    serializer_class = OperatorSerializer


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client
    serializer_class = ClientSerializer


class ClientDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client
    serializer_class = ClientSerializer