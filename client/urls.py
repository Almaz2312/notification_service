from rest_framework.urls import path

from client.views import (
    OperatorDetailDeleteView, OperatorListCreateView,
    ClientListCreateView, ClientDetailUpdateDeleteView
)


urlpatterns = [
    path('', ClientListCreateView.as_view(), name='client'),
    path('<int:pk>', ClientDetailUpdateDeleteView.as_view(), name='client_detail'),
    path('operator/', OperatorListCreateView.as_view(), name='operator'),
    path('operator/<int:pk>', OperatorDetailDeleteView.as_view(), name='operator_detail'),
]
