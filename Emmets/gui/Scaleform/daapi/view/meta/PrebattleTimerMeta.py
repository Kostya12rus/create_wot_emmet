# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrebattleTimerMeta.py
from gui.Scaleform.daapi.view.battle.shared.prebattle_timers.timer_base import PreBattleTimerBase

class PrebattleTimerMeta(PreBattleTimerBase):

    def onShowInfo(self):
        self._printOverrideError('onShowInfo')

    def onHideInfo(self):
        self._printOverrideError('onHideInfo')

    def as_addInfoS(self, linkage, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addInfo(linkage, data)

    def as_setInfoHintS(self, hint):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfoHint(hint)

    def as_showInfoS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showInfo()