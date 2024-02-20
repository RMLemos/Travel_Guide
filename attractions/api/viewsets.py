from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from attractions.models import MustSee
from attractions.api.serializers import MustSeeSerializer

class MustseeViewSet(ModelViewSet):
     queryset = MustSee.objects.all()
     serializer_class = MustSeeSerializer
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['name', 'opening_hours']