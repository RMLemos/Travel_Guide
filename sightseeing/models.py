from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField('Approved', default=False)

    def __str__(self):
        return self.name