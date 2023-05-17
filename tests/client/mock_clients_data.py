import factory
from factory import fuzzy

from client.models import Client, Operator, Tag


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    tag = factory.Faker('sentence')


class OperatorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Operator

    code = factory.Faker('pyint', min_value=0, max_value=999)


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    phone_number = fuzzy.FuzzyText(length=11, chars="0123456789", suffix="7")
    code = factory.SubFactory(OperatorFactory)
    tag = factory.SubFactory(TagFactory)
    timezone = fuzzy.FuzzyChoice(Client.TIMEZONES)

