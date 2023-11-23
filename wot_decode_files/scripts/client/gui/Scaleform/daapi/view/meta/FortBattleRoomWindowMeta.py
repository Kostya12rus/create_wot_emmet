# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBattleRoomWindowMeta.py
from gui.Scaleform.daapi.view.lobby.rally.RallyMainWindowWithSearch import RallyMainWindowWithSearch

class FortBattleRoomWindowMeta(RallyMainWindowWithSearch):

    def onBrowseClanBattles(self):
        self._printOverrideError('onBrowseClanBattles')

    def onJoinClanBattle(self, rallyId, slotIndex, peripheryId):
        self._printOverrideError('onJoinClanBattle')

    def onCreatedBattleRoom(self, battleID, peripheryId):
        self._printOverrideError('onCreatedBattleRoom')

    def refresh(self):
        self._printOverrideError('refresh')

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_setWaitingS(self, visible, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaiting(visible, message)

    def as_setInfoS(self, visible, message, buttonLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(visible, message, buttonLabel)