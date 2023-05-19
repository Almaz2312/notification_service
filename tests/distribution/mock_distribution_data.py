from django.utils import timezone
from django.utils import timezone
import factory

from distribution.models import Distribute
from tests.client.mock_clients_data import OperatorFactory, TagFactory


class DistributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Distribute

    sending_datetime = factory.LazyAttribute(
        lambda _: timezone.datetime.now() + timezone.timedelta(days=1)
    )
    text = factory.Faker("sentence")
    operator_filter = factory.SubFactory(OperatorFactory)
    tag_filter = factory.SubFactory(TagFactory)
    ending_datetime = factory.LazyAttribute(
        lambda _: timezone.datetime.now() + timezone.timedelta(days=2)
    )
