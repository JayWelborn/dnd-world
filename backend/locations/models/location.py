from django.db import models

from shared.models import BaseEntity

class Location(BaseEntity):
    """
    Location in a DnD World.

    Fields:
        parent: int FK to parent location, if applicable
    """

    parent = models.ForeignKey("Location", blank=True, null=True, on_delete=models.SET_NULL)
