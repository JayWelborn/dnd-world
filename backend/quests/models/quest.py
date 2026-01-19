from django.db import models

from shared.models import BaseEntity

from .quest_character import QuestCharacter

# Create your models here.
class Quest(BaseEntity):
    """
    Quest given or to be given to PCs

    Fields:
        giver: Person - person who gave the party the quest
        given_location: Location - where did the party receive the quest
        location: Location - where does the quest begin/take place
        status: QuestStatuses - status of the quest
        characters: QuestCharacter[] - who is important to this quest
    """

    class QuestStatuses(models.TextChoices):
        NOT_GIVEN = 'not_given', 'Not Given'
        GIVEN = 'given', 'Given'
        NOT_STARTED = 'not_started', 'Not Started'
        IN_PROGRESS = 'in_progress', 'In Progress'
        FAILED = 'failed', 'Failed'
        SUCCEEDED = 'succeeded', 'Succeeded'
        ABANDONED = 'abandoned', 'Abandoned'
        ENDED = 'ended', 'Ended'
    
    giver = models.ForeignKey(to='people.Person', blank=True, null=True, on_delete=models.SET_NULL, related_name='quests_given')
    given_location = models.ForeignKey(to='locations.Location', blank=True, null=True, on_delete=models.SET_NULL, related_name='quests_given_here')
    location = models.ForeignKey(to='locations.Location', on_delete=models.CASCADE, related_name='quests_here')
    status = models.CharField(max_length=24, choices=QuestStatuses, default=QuestStatuses.NOT_GIVEN)
    characters = models.ManyToManyField(to='people.Person', through=QuestCharacter, related_name='quest_appearances')
