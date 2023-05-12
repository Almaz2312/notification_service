from rest_framework.urls import path

from distribution.views import (
    DistributionListCreateView, DistributionDetailUpdateDeleteView
)


urlpatterns = [
    path('', DistributionListCreateView.as_view(), name='distribution'),
    path('<int:pk>', DistributionDetailUpdateDeleteView.as_view(), name='distribution_detail'),
]