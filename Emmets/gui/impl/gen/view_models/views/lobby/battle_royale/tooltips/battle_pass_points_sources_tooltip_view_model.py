# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_royale/tooltips/battle_pass_points_sources_tooltip_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_royale.tooltips.battle_pass_quests_points import BattlePassQuestsPoints

class BattlePassPointsSourcesTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattlePassPointsSourcesTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getBattlePoints(self):
        return self._getNumber(0)

    def setBattlePoints(self, value):
        self._setNumber(0, value)

    def getQuestPoints(self):
        return self._getArray(1)

    def setQuestPoints(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(BattlePassPointsSourcesTooltipViewModel, self)._initialize()
        self._addNumberProperty('battlePoints', 0)
        self._addArrayProperty('questPoints', Array())