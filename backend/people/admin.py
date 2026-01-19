from django.contrib import admin

from people.models.person import Person
from people.models.location_role import LocationRole

admin.site.register(Person)
admin.site.register(LocationRole)
