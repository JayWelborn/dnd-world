from django.db import models

from shared.models import BaseEntity

class QuestCharacter(BaseEntity):
    """
    QuestCharacter marks an person as appearing within a quest

    Fields:
        character: Person
        role: str - what role does the person play in the quest
    """
    character = models.ForeignKey(to='people.Person', on_delete=models.CASCADE)
    quest = models.ForeignKey(to='quests.Quest', on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
