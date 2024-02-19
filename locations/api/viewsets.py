from rest_framework import viewsets
from locations.models import Address
from locations.api.serializers import AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
     queryset = Address.objects.all()
     serializer_class = AddressSerializer