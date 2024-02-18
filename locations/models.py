from django.db import models

class Address(models.Model):
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    address = models.CharField(max_length=150) 
    city = models.CharField(max_length=150) 
    country = models.CharField(max_length=150) 
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.address
