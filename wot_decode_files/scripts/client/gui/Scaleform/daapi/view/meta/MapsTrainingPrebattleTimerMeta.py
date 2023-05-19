# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MapsTrainingPrebattleTimerMeta.py
from gui.Scaleform.daapi.view.battle.shared.prebattle_timers.timer_base import PreBattleTimerBase

class MapsTrainingPrebattleTimerMeta(PreBattleTimerBase):

    def as_updateS(self, data, text):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data, text)

    def as_setSideS(self, side):
        if self._isDAAPIInited():
            return self.flashObject.as_setSide(side)