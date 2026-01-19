from django.db import models

from shared.models import BaseEntity

# Create your models here.
class Person(BaseEntity):
    """
    Person in the DnD world
    """

    race = models.TextField(max_length=48, blank=True, null=True, default="Human")
    dnd_class = models.TextField(max_length=255, blank=True, null=True)
    stat_block = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='people/%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'People'
