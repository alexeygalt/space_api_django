from rest_framework import serializers

from indication.models import Indication, User


class IndicationSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Indication
        fields = '__all__'


class IndicationCreateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Indication
        fields = '__all__'
