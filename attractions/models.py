from django.db import models

class MustSee(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.TextField()
    min_age = models.IntegerField()

    def __str__(self):
        return self.name
