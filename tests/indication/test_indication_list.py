import pytest

from indication.serializators.indication import IndicationSerializer
from tests.factories.indication import IndicationFactory


@pytest.mark.django_db
def test_list_indications(client):
    indications = IndicationFactory.create_batch(5)

    expected_response = IndicationSerializer(indications, many=True).data

    response = client.get('/indications/')
    assert response.status_code == 200
    assert response.data == expected_response
