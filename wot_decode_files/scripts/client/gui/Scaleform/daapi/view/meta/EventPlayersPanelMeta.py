# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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

    def as_setPlayerResurrectS(self, vehID, isResurrect):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerResurrect(vehID, isResurrect)

    def as_setPlayerPanelCountPointsS(self, vehID, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelCountPoints(vehID, count)