from django.contrib import admin

from quests.models.quest import Quest
from quests.models.quest_character import QuestCharacter

# Register your models here.
admin.site.register(Quest)
admin.site.register(QuestCharacter)
