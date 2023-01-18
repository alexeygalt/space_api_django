import pytest


@pytest.mark.django_db
def test_create_user(client):
    data = {
        "username": "test",
        "password": "test_password"
    }

    response = client.post(
        '/users/create/',
        data,
        content_type='application/json'
    )
    assert response.status_code == 201
    assert response.data['username'] == "test"
