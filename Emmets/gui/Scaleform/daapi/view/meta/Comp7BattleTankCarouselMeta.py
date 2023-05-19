# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/Comp7BattleTankCarouselMeta.py
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import CarouselEnvironment

class Comp7BattleTankCarouselMeta(CarouselEnvironment):

    def setFilter(self, id):
        self._printOverrideError('setFilter')

    def onViewIsHidden(self):
        self._printOverrideError('onViewIsHidden')

    def as_rowCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_rowCount(value)

    def as_hideS(self, useAnim):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(useAnim)