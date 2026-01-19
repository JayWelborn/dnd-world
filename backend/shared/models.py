from django.db import models

# Create your models here.
class BaseEntity(models.Model):
    """
    Base model proivides the following:
        id: int - auto-increment integer PK for DB optimization
        uuid: str - UUID used for public-facing features
        name: str - entity name
        notes: text - DM notes about entity

    Base model cannot be instantiated on its own.
    """

    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True