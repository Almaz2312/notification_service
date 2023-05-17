import datetime
import factory

from distribution.models import Distribute
from tests.client.mock_clients_data import OperatorFactory, TagFactory


class DistributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Distribute

    sending_datetime = factory.LazyAttribute(
        lambda _: datetime.date.today() + datetime.timedelta(days=1)
    )
    text = factory.Faker("text")
    operator_filter = factory.SubFactory(OperatorFactory)
    tag_filter = factory.SubFactory(TagFactory)
    ending_datetime = factory.LazyAttribute(
        lambda _: datetime.date.today() + datetime.timedelta(days=2)
    )
