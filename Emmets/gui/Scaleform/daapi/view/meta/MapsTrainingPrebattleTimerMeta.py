# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MapsTrainingPrebattleTimerMeta.py
from gui.Scaleform.daapi.view.battle.shared.prebattle_timers.timer_base import PreBattleTimerBase

class MapsTrainingPrebattleTimerMeta(PreBattleTimerBase):

    def as_updateS(self, data, text):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data, text)

    def as_setSideS(self, side):
        if self._isDAAPIInited():
            return self.flashObject.as_setSide(side)