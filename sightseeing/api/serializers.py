from rest_framework import serializers
from sightseeing.models import Place
from attractions.api.serializers import MustSeeSerializer
from locations.api.serializers import AddressSerializer


class PlaceSerializer(serializers.ModelSerializer):

    must_see = MustSeeSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta: 
        model = Place
        fields = '__all__'