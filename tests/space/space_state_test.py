import pytest

from space.serializers import StationDetailSerializer
from tests.factories.station import StationFactory


@pytest.mark.django_db
def test_station_position(client, user_token):
    station = StationFactory.create()

    expected_response = StationDetailSerializer(station).data

    response = client.get(
        f'/stations/{station.pk}/state/',
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_station_position_changed(client, user_token):
    station = StationFactory.create()
    data = {
        "user": "user",
        "axis": "x",
        "distance": 100

    }
    expected_response = {
        'x': 200,
        'y': 100,
        'z': 100
    }

    response = client.patch(
        f'/stations/{station.pk}/state/',
        data,
        HTTP_AUTHORIZATION="Bearer " + user_token,
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_station_position_broken(client, user_token):
    station = StationFactory.create()
    data = {
        "user": "user",
        "axis": "x",
        "distance": -500

    }
    expected_response = {
        'x': -400,
        'y': 100,
        'z': 100
    }

    response = client.patch(
        f'/stations/{station.pk}/state/',
        data,
        HTTP_AUTHORIZATION="Bearer " + user_token,
        content_type="application/json"
    )
    response_two = client.get(f'/stations/{station.pk}/')

    assert response.status_code == 200
    assert response.data == expected_response
    assert response_two.data['condition'] == 'broken'
    assert response_two.data['date_broken'] is not None


@pytest.mark.django_db
def test_station_position_not_valid_data(client, user_token):
    station = StationFactory.create()
    data = {
        "user": "user",
        "distance": 100

    }
    expected_response = {
        "error": "not valid data"
    }

    response = client.patch(
        f'/stations/{station.pk}/state/',
        data,
        HTTP_AUTHORIZATION="Bearer " + user_token,
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db
def test_station_position_not_found(client, user_token):
    station = StationFactory.create()

    expected_response = {
        "error": "station dont exist"
    }

    response = client.get(
        f'/stations/2/state/',
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db
def test_station_position_not_authorized(client):
    station = StationFactory.create()

    response = client.get(
        f'/stations/{station.pk}/state/',

    )

    assert response.status_code == 401
