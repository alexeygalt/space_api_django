import pytest
from datetime import datetime
from space.serializers import StationSerializer
from tests.factories.station import StationFactory


@pytest.mark.django_db
def test_station_retrieve(client):
    station = StationFactory.create()
    response = client.get(
        f"/stations/{station.pk}/",

    )
    assert response.status_code == 200
    assert response.data == StationSerializer(station).data


@pytest.mark.django_db
def test_station_retrieve_update(client):
    station = StationFactory.create()
    data = {
        "name": "update",
    }
    expected_response = {
        "id": 1,
        "name": "update",
        "condition": "running",
        "date_created": datetime.now().strftime("%Y-%m-%d"),
        "date_broken": None,
    }

    response = client.patch(
        f"/stations/{station.pk}/",
        data,
        content_type='application/json'

    )
    assert response.status_code == 200
    assert response.data == expected_response
    assert station.x == 100
    assert station.y == 100
    assert station.z == 100


@pytest.mark.django_db
def test_station_retrieve_delete(client):
    station = StationFactory.create()

    response = client.delete(
        f"/stations/{station.pk}/",

    )
    assert response.status_code == 204
    assert response.data is None


@pytest.mark.django_db
def test_station_retrieve_not_valid_values(client):
    station = StationFactory.create()
    data = {
        "name": "update",
        "condition": "broken",
        "date_broken": datetime.now().strftime("%Y-%m-%d")
    }
    expected_response = {
        "id": 1,
        "name": "update",
        "condition": "running",
        "date_created": datetime.now().strftime("%Y-%m-%d"),
        "date_broken": None,
    }
    response = client.put(
        f"/stations/{station.pk}/",
        data,
        content_type="application/json"

    )
    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_station_retrieve_not_found(client):
    station = StationFactory.create()

    expected_response = {

        "detail": "Not found."
    }

    response = client.get(
        f"/stations/2/",

    )
    assert response.status_code == 404
    assert response.data == expected_response
