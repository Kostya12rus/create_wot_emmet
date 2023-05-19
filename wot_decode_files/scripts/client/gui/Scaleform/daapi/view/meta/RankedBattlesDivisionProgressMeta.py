# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesDivisionProgressMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesDivisionProgressMeta(BaseDAAPIComponent):

    def as_setStatsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatsData(data)

    def as_setBonusBattlesLabelS(self, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setBonusBattlesLabel(label)

    def as_setRankedDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRankedData(data)

    def as_setDivisionStatusS(self, title, description):
        if self._isDAAPIInited():
            return self.flashObject.as_setDivisionStatus(title, description)