
from pytest_factoryboy import register

from tests.factories.indication import IndicationFactory
from tests.factories.station import StationFactory
from tests.factories.user import UserFactory

register(StationFactory)
register(IndicationFactory)
register(UserFactory)

pytest_plugins = "tests.fixtures"