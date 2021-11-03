# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventPlayersPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventPlayersPanelMeta(BaseDAAPIComponent):

    def as_setPlayerPanelInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelInfo(data)

    def as_setPlayerPanelHpS(self, vehID, hpMax, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelHp(vehID, hpMax, hpCurrent)

    def as_setPlayerDeadS(self, vehID):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerDead(vehID)

    def as_setPlayerPanelCountSoulsS(self, vehID, countSouls):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelCountSouls(vehID, countSouls)

    def as_setCollectorGoalS(self, goal):
        if self._isDAAPIInited():
            return self.flashObject.as_setCollectorGoal(goal)

    def as_setCollectorNeedValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCollectorNeedValue(value)

    def as_updateTriggeredChatCommandsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTriggeredChatCommands(data)

    def as_setChatCommandS(self, vehicleID, chatCommand, chatCommandFlags):
        if self._isDAAPIInited():
            return self.flashObject.as_setChatCommand(vehicleID, chatCommand, chatCommandFlags)