# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fun_random/tooltips/quests_preview_tooltip.py
from gui.server_events import events_helpers
from gui.server_events.events_helpers import isFunRandomQuest
from gui.shared.tooltips.quests import QuestsPreviewTooltipData
from helpers import dependency
from skeletons.gui.game_control import IFunRandomController

class FunRandomQuestsPreviewTooltip(QuestsPreviewTooltipData):
    __funRandomCtrl = dependency.descriptor(IFunRandomController)

    def _getQuests(self, vehicle):
        if self.__funRandomCtrl.isSuitableVehicle(vehicle) is not None:
            return []
        else:
            quests = [ q for q in self._questController.getQuestForVehicle(vehicle) if isFunRandomQuest(q.getID()) and q.shouldBeShown() and not q.isCompleted() ]
            return sorted(quests, key=events_helpers.questsSortFunc)

    def _isShowBottom(self, vehicle=None):
        if self.__funRandomCtrl.isSuitableVehicle(vehicle) is not None:
            return ''
        else:
            return super(FunRandomQuestsPreviewTooltip, self)._isShowBottom()