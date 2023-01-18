from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView

from indication.models import Indication
from indication.serializators.indication import IndicationSerializer


@extend_schema(
    description="Retrieve indication's list",
    summary="Show all indications"
)
class IndicationListView(ListAPIView):
    """get all indications"""
    queryset = Indication.objects.all()
    serializer_class = IndicationSerializer


@extend_schema(
    description="Retrieve one indigation by pk",
    summary="Get one indication"
)
class IndicationDetailView(RetrieveAPIView):
    """get indication by pk"""
    queryset = Indication.objects.all()
    serializer_class = IndicationSerializer
