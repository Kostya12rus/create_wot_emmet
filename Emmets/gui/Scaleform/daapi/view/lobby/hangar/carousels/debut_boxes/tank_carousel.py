# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/debut_boxes/tank_carousel.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels import BattlePassTankCarousel

class DebutBoxesTankCarousel(BattlePassTankCarousel):

    def _getFilters(self):
        return super(DebutBoxesTankCarousel, self)._getFilters() + ('debut_boxes', )

    def getCustomParams(self):
        data = super(DebutBoxesTankCarousel, self).getCustomParams()
        data.update({'debut_boxes': True})
        return data