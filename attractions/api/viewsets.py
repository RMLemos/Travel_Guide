from rest_framework import viewsets
from attractions.models import MustSee
from attractions.api.serializers import MustSeeSerializer

class MustseeViewSet(viewsets.ModelViewSet):
     queryset = MustSee.objects.all()
     serializer_class = MustSeeSerializer