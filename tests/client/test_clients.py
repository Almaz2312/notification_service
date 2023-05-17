import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy

from client.models import Operator, Tag, Client
from tests.client.mock_clients_data import (
    TagFactory,
    OperatorFactory,
    ClientFactory
)

pytestmark = pytest.mark.django_db


class TestClientView:
    def test_client_list_view(self, api_client):
        ClientFactory.create_batch(size=5)
        response = api_client.get(reverse_lazy("client"))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == Client.objects.all().count()

    def test_client_create_view(self, api_client):
        tag = TagFactory.create()
        operator_code = OperatorFactory.create()
        data = {"phone_number": "71231231231", "tag": tag.id, "code": operator_code.id, "timezone": "UTC"}
        response = api_client.post(reverse_lazy("client"), data=data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["tag"] == data["tag"]

    def test_client_detail_view(self, api_client):
        client = ClientFactory.create()

        response = api_client.get(reverse_lazy("client_detail", kwargs={"pk": client.id}))

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["phone_number"] == client.phone_number

    def test_client_update_view(self, api_client):
        client = ClientFactory.create()
        data = {"phone_number": "70987654321"}
        response = api_client.patch(reverse_lazy("client_detail", kwargs={"pk": client.id}), data=data, follow=True)

        assert response.status_code == status.HTTP_202_ACCEPTED
        assert response.json()["phone_number"] == data["phone_number"]

    def test_client_delete_view(self, api_client):
        client = ClientFactory.create()
        response = api_client.delete(reverse_lazy("client_detail", kwargs={"pk": client.id}))

        assert Client.objects.all().count() == 0
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestOperatorView:
    def test_operator_list_view(self, api_client):
        OperatorFactory.create_batch(size=7)
        response = api_client.get(reverse_lazy("operator"))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == Operator.objects.all().count()

    def test_operator_create_view(self, api_client):
        data = {"code": 555}
        response = api_client.post(reverse_lazy("operator"), data=data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["code"] == data["code"]

    def test_operator_detail_view(self, api_client):
        operator = OperatorFactory.create()
        response = api_client.get(reverse_lazy("operator_detail", kwargs={"pk": operator.id}))

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["code"] == operator.code

    def test_operator_put_update_view(self, api_client):
        operator = OperatorFactory.create()
        data = {"code": 555}
        response = api_client.patch(reverse_lazy("operator_detail", kwargs={"pk": operator.id}), data=data, follow=True)

        assert response.status_code == status.HTTP_202_ACCEPTED
        assert response.json()["code"] == data["code"]

    def test_operator_delete_view(self, api_client):
        operator = OperatorFactory.create()
        response = api_client.delete(reverse_lazy("operator_detail", kwargs={"pk": operator.id}), follow=True)

        assert response.status_code == status.HTTP_204_NO_CONTENT

