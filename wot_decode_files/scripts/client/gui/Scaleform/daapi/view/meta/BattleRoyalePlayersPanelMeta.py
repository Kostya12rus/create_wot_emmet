# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyalePlayersPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleRoyalePlayersPanelMeta(BaseDAAPIComponent):

    def switchToPlayer(self, vehicleID):
        self._printOverrideError('switchToPlayer')

    def as_setPlayersDataS(self, data, lostIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayersData(data, lostIndex)

    def as_setSeparatorVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setSeparatorVisibility(isVisible)