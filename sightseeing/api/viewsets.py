from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from sightseeing.models import Place
from sightseeing.api.serializers import PlaceSerializer

class PlaceViewSet(ModelViewSet):
     serializer_class = PlaceSerializer
     filter_backends = [filters.SearchFilter]
     search_fields = ['name', 'address__city']

     def get_queryset(self):
          return Place.objects.filter(status=True)