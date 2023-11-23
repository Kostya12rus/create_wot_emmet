# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesLeaguesViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesLeaguesViewMeta(BaseDAAPIComponent):

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setStatsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatsData(data)

    def as_setEfficiencyDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setEfficiencyData(data)

    def as_setRatingDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRatingData(data)

    def as_setBonusBattlesLabelS(self, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setBonusBattlesLabel(label)