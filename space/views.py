from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView

from indication.serializators.indication import IndicationCreateSerializer
from space.models import Station
from space.serializers import StationSerializer, StationDetailSerializer
from rest_framework.permissions import IsAuthenticated


@extend_schema_view(
    list=extend_schema(
        description='Retrieve space list',
        summary='Space list'
    ),
    create=extend_schema(
        description='Create new Space object',
        summary='Create Station'
    ),
    retrieve=extend_schema(
        description="Get Station by pk",
        summary='Get one station'
    ),
    update=extend_schema(
        description="Update Station by pk",
        summary="Update one station"
    ),
    partial_update=extend_schema(
        description="Partial update Station by pk",
        summary="Partial update one Station"
    ),
    destroy=extend_schema(
        description="Delete one station by pk",
        summary="Delete one Station"
    )
)
class StationViewSet(viewsets.ModelViewSet):
    """viewset to Station model with all methods"""
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationCreateView(RetrieveUpdateAPIView):
    """set position param to station and add indication to db"""
    queryset = Station.objects.all()
    serializer_class = StationDetailSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'patch']

    @extend_schema(
        description="Retrieve Station's coordinates ",
        summary="Get Coordinates"
    )
    def get(self, request, *args, **kwargs):
        if Station.objects.filter(pk=kwargs['pk']):
            return self.retrieve(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'station dont exist'})

    @extend_schema(
        description="Update Station's coordinates ",
        summary="Update Coordinates"
    )
    def patch(self, request, *args, **kwargs):
        if Station.objects.filter(pk=kwargs['pk']):
            serializer = IndicationCreateSerializer(data=request.data)
            if not serializer.is_valid():
                return JsonResponse({'error': 'not valid data'})
            serializer.save()
            station = Station.objects.get(pk=kwargs['pk'])
            position = request.data.get('axis')
            distance = request.data.get('distance')

            if position == 'x':
                station.x += distance
            elif position == 'y':
                station.y += distance
            elif position == 'z':
                station.z += distance
            if not all([item > 0 for item in (int(station.x), int(station.y), int(station.z))]):
                station.condition = 'broken'
                from datetime import datetime
                station.date_broken = datetime.now()
            station.save()
            return self.partial_update(request, *args, **kwargs)

        else:
            return JsonResponse({'error': 'station dont exist'})
