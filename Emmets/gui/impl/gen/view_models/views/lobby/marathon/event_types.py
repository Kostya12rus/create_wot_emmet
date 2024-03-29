# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/marathon/event_types.py
from frameworks.wulf import ViewModel

class EventTypes(ViewModel):
    __slots__ = ()
    BATTLE_QUEST = 'battleQuest'
    RESEARCH_VEHICLE = 'researchVehicle'
    RESEARCH_MODULE = 'researchModule'
    CREW_MEMBER_NEW_SKILL = 'crewMemberNewSkill'
    PERSONAL_MISSION = 'personalQuest'
    DAILY_QUEST = 'dailyQuest'
    RANKED_BATTLES = 'rankedBattles'
    BATTLE_PASS = 'battlePass'

    def __init__(self, properties=0, commands=0):
        super(EventTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(EventTypes, self)._initialize()