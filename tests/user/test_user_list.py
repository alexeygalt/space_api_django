import pytest

from tests.factories.user import UserFactory


@pytest.mark.django_db
def test_list_users(client):
    users = UserFactory.create_batch(2)
    response = client.get('/users/')

    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_create_user_unique_name(client):
    expected_response = {
        "username": [
            "A user with that username already exists."
        ]
    }

    data = {
        "username": "test",
        "password": "test_password"

    }
    response = client.post(
        '/users/create/',
        data,
        content_type='application/json'
    )
    response_two = client.post(
        '/users/create/',
        data,
        content_type='application/json'
    )
    assert response_two.status_code == 400
    assert response_two.data == expected_response
