import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy

from message.models import Message
from tests.message.mock_message_data import MessageFactory


pytestmark = pytest.mark.django_db


class TestMessageView:
    def test_list_view(self, api_client):
        MessageFactory.create_batch(size=5)
        response = api_client.get(reverse_lazy("message"))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == Message.objects.all().count()
