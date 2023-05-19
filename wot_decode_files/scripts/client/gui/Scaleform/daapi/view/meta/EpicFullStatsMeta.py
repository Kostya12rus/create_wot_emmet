# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicFullStatsMeta.py
from gui.Scaleform.daapi.view.battle.shared.base_stats import StatsBase

class EpicFullStatsMeta(StatsBase):

    def as_initializeTextS(self, myLaneText, allLanesText):
        if self._isDAAPIInited():
            return self.flashObject.as_initializeText(myLaneText, allLanesText)

    def as_setIsInteractiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsInteractive(value)