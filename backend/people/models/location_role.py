from django.db import models

from shared.models import BaseEntity

class LocationRole(BaseEntity):
    """
    Relationship between a person and a location.

    Fields:
        location: Location - where the role exists
        person: Person - who does this role in that location
    """

    location = models.ForeignKey("locations.Location", blank=True, null=True, on_delete=models.SET_NULL)
    person = models.ForeignKey("people.Person", on_delete=models.CASCADE)
    