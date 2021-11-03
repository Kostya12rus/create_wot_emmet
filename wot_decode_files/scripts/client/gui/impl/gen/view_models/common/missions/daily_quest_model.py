# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/daily_quest_model.py
from gui.impl.gen.view_models.common.missions.quest_model import QuestModel

class DailyQuestModel(QuestModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(DailyQuestModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getString(11)

    def setIcon(self, value):
        self._setString(11, value)

    def _initialize(self):
        super(DailyQuestModel, self)._initialize()
        self._addStringProperty('icon', '')