import factory.django

from space.models import Station


class StationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Station

    name = factory.Faker('name')
