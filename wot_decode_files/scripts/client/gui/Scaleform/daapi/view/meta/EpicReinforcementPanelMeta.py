# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicReinforcementPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EpicReinforcementPanelMeta(BaseDAAPIComponent):

    def as_setPlayerLivesS(self, lives):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerLives(lives)

    def as_setTimestampS(self, timestamp, servertime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimestamp(timestamp, servertime)

    def as_setTimeS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setTime(time)