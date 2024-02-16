from django.contrib.auth.models import User
from django.db import models
from sightseeing.models import Place

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField('Comment', blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField('Approved', default=True)
    place = models.ForeignKey(Place, related_name='placecomment', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    place = models.ForeignKey(Place, related_name='placerating', on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating: {self.get_rating_display()}"
