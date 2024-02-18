from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify

from attractions.models import MustSee
from locations.models import Address


class Place(models.Model):
    name = models.CharField('Name', max_length=150)
    description = models.TextField('Description', max_length=255)
    status = models.BooleanField('Approved', default=False)
    slug = models.SlugField('Slug', unique=True, default=None, null=True, blank=True, max_length=255)
    must_see = models.ManyToManyField(MustSee, verbose_name='Must-see', blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
def place_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(place_pre_save, sender=Place)