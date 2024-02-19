from rest_framework import serializers
from attractions.models import MustSee


class MustSeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MustSee
        fields = '__all__'