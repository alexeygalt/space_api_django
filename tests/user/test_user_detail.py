import pytest

from indication.serializators.user import UserSerializer
from tests.factories.user import UserFactory


@pytest.mark.django_db
def test_user_retrieve(client):
    user = UserFactory.create()
    response = client.get(
        f"/users/{user.pk}",

    )
    assert response.status_code == 200
    assert response.data == UserSerializer(user).data