# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CarouselEnvironmentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CarouselEnvironmentMeta(BaseDAAPIComponent):

    def selectVehicle(self, id):
        self._printOverrideError('selectVehicle')

    def resetFilters(self):
        self._printOverrideError('resetFilters')

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabled(value)

    def as_showCounterS(self, countText, isAttention):
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText, isAttention)

    def as_hideCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideCounter()

    def as_blinkCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkCounter()