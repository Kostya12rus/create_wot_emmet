# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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