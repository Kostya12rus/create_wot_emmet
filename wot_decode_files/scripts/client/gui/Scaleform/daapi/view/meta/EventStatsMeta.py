# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventStatsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventStatsMeta(BaseDAAPIComponent):

    def as_updatePlayerStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerStats(data)

    def as_updateDataS(self, title, desc, difficulty, goal):
        if self._isDAAPIInited():
            return self.flashObject.as_updateData(title, desc, difficulty, goal)

    def as_updateBuffsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBuffs(data)