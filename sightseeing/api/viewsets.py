from rest_framework import viewsets
from sightseeing.models import Place
from sightseeing.api.serializers import PlaceSerializer

class PlaceViewSet(viewsets.ModelViewSet):
     queryset = Place.objects.all()
     serializer_class = PlaceSerializer