from rest_framework import serializers
from reviews.models import Comment
from reviews.models import Rating


class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Rating
        fields = '__all__'