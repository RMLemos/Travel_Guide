from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify

class MustSee(models.Model):

    class Meta:
        verbose_name = 'Must-see'
        verbose_name_plural = 'Must-see'

    name = models.CharField('Name', max_length=50)
    slug = models.SlugField('Slug', unique=True, default=None, null=True, blank=True, max_length=255)
    description = models.TextField('Description')
    opening_hours = models.TextField('Opening hours')
    min_age = models.IntegerField('Minimun Age')
    image = models.ImageField(upload_to='attractions', null=True, blank=True)

    def __str__(self):
        return self.name


def mustsee_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(mustsee_pre_save, sender=MustSee)
