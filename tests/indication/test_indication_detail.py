import pytest

from indication.serializators.indication import IndicationSerializer
from tests.factories.indication import IndicationFactory


@pytest.mark.django_db
def test_indication_retrieve(client):
    indication = IndicationFactory.create()

    response = client.get(
        f"/indications/{indication.pk}",

    )

    assert response.status_code == 200
    assert response.data == IndicationSerializer(indication).data
