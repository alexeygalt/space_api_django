from datetime import datetime

import pytest


@pytest.mark.django_db
def test_create_station(client):
    expected_response = {
        "id": 1,
        "name": "test_station",
        "condition": "running",
        "date_created": datetime.now().strftime("%Y-%m-%d"),
        "date_broken": None,
    }
    data = {
        "name": "test_station"
    }
    response = client.post(
        '/stations/',
        data,
        content_type='application/json'
    )
    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_station_unique_name(client):
    expected_response = {
        "name": [
            "Станция with this name already exists."
        ]
    }

    data = {
        "name": "test_station"
    }
    response = client.post(
        '/stations/',
        data,
        content_type='application/json'
    )
    response_two = client.post(
        '/stations/',
        data,
        content_type='application/json'
    )
    assert response_two.status_code == 400
    assert response_two.data == expected_response


@pytest.mark.django_db
def test_create_station_broken_status(client):
    expected_response = {
        "id": 1,
        "name": "test_station",
        "condition": "running",
        "date_created": datetime.now().strftime("%Y-%m-%d"),
        "date_broken": None,
    }
    data = {
        "name": "test_station",
        "condition": "broken",
    }
    response = client.post(
        '/stations/',
        data,
        content_type='application/json'
    )
    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_station_broken_date(client):
    expected_response = {
        "id": 1,
        "name": "test_station",
        "condition": "running",
        "date_created": datetime.now().strftime("%Y-%m-%d"),
        "date_broken": None,
    }
    data = {
        "name": "test_station",
        "date_broken": datetime.now().strftime("%Y-%m-%d")
    }
    response = client.post(
        '/stations/',
        data,
        content_type='application/json'
    )
    assert response.status_code == 201
    assert response.data == expected_response

