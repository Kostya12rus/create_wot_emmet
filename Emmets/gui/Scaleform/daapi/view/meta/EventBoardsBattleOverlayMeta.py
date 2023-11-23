# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventBoardsBattleOverlayMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventBoardsBattleOverlayMeta(BaseDAAPIComponent):

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setExperienceDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setExperienceData(data)

    def as_setStatisticsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatisticsData(data)

    def as_setTableHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeaderData(data)

    def as_setTableDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTableData(data)