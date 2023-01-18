import pytest

from space.serializers import StationSerializer
from tests.factories.station import StationFactory


@pytest.mark.django_db
def test_list_stations(client):
    stations = StationFactory.create_batch(5)

    expected_response = StationSerializer(stations, many=True).data

    response = client.get('/stations/')
    assert response.status_code == 200
    assert response.data == expected_response
