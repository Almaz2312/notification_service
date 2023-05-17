import datetime

import faker
import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy

from distribution.models import Distribute
from tests.client.mock_clients_data import TagFactory, OperatorFactory
from tests.distribution.mock_distribution_data import DistributeFactory

pytestmark = pytest.mark.django_db


class TestDistributeView:
    def test_list_view(self, api_client):
        DistributeFactory.create_batch(size=5)
        response = api_client.get(reverse_lazy("distribution"))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == Distribute.objects.all().count()

    def test_create_view(self, api_client):
        tag = TagFactory.create()
        operator = OperatorFactory.create()
        data = {"sending_datetime": datetime.datetime.now(), "text": faker.Faker("text"),
                "operator_filter": operator.id, "tag_filter": tag.id,
                "ending_datetime": datetime.date.today() + datetime.timedelta(days=1)}
        response = api_client.post(reverse_lazy("distribution"), data=data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["text"] == data["text"]

    def test_detail_view(self, api_client):
        distribution = DistributeFactory.create()
        response = api_client.get(reverse_lazy("distribution_detail", kwargs={"pk": distribution.id}))

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["text"] == distribution.text

    def test_update_view(self, api_client):
        distribution = DistributeFactory.create()
        data = {"text": faker.Faker("text")}
        response = api_client.patch(
            reverse_lazy(
                "distribution_detail", kwargs={"pk": distribution.id}
            ),
            data=data, follow=True
        )

        assert response.status_code == status.HTTP_202_ACCEPTED
        assert response.json()["text"] == data["text"]

    def test_delete_view(self, api_client):
        distribution = DistributeFactory.create()
        response = api_client.delete(reverse_lazy("distribution_detail", kwargs={"pk": distribution.id}))

        assert response.status_code == status.HTTP_204_NO_CONTENT
