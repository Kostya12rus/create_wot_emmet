# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicBattlePageMeta.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class EpicBattlePageMeta(ClassicPage):

    def as_setSelectReservesAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectReservesAvailable(value)

    def as_setVehPostProgressionEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehPostProgressionEnabled(value)