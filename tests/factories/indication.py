import factory.django

from indication.models import Indication
from tests.factories.user import UserFactory


class IndicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Indication

    user = factory.SubFactory(UserFactory)
    axis = 'z'
    distance = 100
