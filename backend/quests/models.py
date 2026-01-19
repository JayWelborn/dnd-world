from django.db import models

from shared.models import BaseEntity

# Create your models here.
class Quest(BaseEntity):
    """
    Quest given or to be given to PCs
    """

    class QuestStatuses(models.TextChoices):
        NOT_GIVEN = 'not_given', 'Not Given'
        GIVEN = 'given', 'Given'
        NOT_STARTED = 'not_started', 'Not Started'
        ABANDONED = 'abandoned', 'Abandoned'
        IN_PROGRESS = 'in_progress', 'In Progress'
        FAILED = 'failed', 'Failed'
        SUCCEEDED = 'succeeded', 'Succeeded'
        ENDED = 'ended', 'Ended'
    
    giver = models.ForeignKey(to='people.Person', blank=True, null=True, on_delete=models.SET_NULL, related_name='quests_given')
    given_location = models.ForeignKey(to='locations.Location', blank=True, null=True, on_delete=models.SET_NULL, related_name='quests_given_here')
    location = models.ForeignKey(to='locations.Location', on_delete=models.CASCADE, related_name='quests_here')
    status = models.CharField(max_length=24, choices=QuestStatuses, default=QuestStatuses.NOT_GIVEN)
