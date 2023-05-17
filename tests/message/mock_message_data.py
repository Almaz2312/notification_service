import datetime
import factory
from factory import fuzzy

from message.models import Message
from tests.distribution.mock_distribution_data import DistributeFactory
from tests.client.mock_clients_data import ClientFactory


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    created_datetime = datetime.datetime.now()
    status = fuzzy.FuzzyChoice(choices=[True, False])
    distribution = factory.SubFactory(DistributeFactory)
    client = factory.SubFactory(ClientFactory)