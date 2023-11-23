# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/rewards_selection_view_model.py
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_base_model import SelectableRewardBaseModel

class RewardsSelectionViewModel(SelectableRewardBaseModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RewardsSelectionViewModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)

    def getChapterID(self):
        return self._getNumber(2)

    def setChapterID(self, value):
        self._setNumber(2, value)

    def getIsExtra(self):
        return self._getBool(3)

    def setIsExtra(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(RewardsSelectionViewModel, self)._initialize()
        self._addNumberProperty('level', 0)
        self._addNumberProperty('chapterID', 0)
        self._addBoolProperty('isExtra', False)