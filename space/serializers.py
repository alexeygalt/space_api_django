from rest_framework import serializers

from space.models import Station


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        exclude = ['x', 'y', 'z']
        read_only_fields = ['condition', 'date_broken']


class StationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['x', 'y', 'z']


