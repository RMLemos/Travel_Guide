from rest_framework import viewsets
from reviews.models import Comment
from reviews.models import Rating
from reviews.api.serializers import RatingSerializer
from reviews.api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
     queryset = Comment.objects.all()
     serializer_class = CommentSerializer


class RatingViewSet(viewsets.ModelViewSet):
     queryset = Rating.objects.all()
     serializer_class = RatingSerializer