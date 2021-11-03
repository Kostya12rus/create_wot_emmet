# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/epic/epic_quest_reward_model.py
from frameworks.wulf import ViewModel

class EpicQuestRewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(EpicQuestRewardModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)

    def getItemSource(self):
        return self._getString(1)

    def setItemSource(self, value):
        self._setString(1, value)

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(EpicQuestRewardModel, self)._initialize()
        self._addStringProperty('value', '')
        self._addStringProperty('itemSource', '')
        self._addStringProperty('description', '')