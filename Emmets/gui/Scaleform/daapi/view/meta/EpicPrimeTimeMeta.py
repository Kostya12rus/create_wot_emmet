# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicPrimeTimeMeta.py
from gui.Scaleform.daapi.view.lobby.prime_time_view_base import PrimeTimeViewBase

class EpicPrimeTimeMeta(PrimeTimeViewBase):

    def as_setHeaderTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderText(value)

    def as_setBackgroundSourceS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackgroundSource(source)