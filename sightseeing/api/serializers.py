from rest_framework import serializers
from sightseeing.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Place
        fields = '__all__'