# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/comp7/tank_carousel.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels import BattlePassTankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.comp7.carousel_data_provider import Comp7CarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.comp7.carousel_filter import Comp7CarouselFilter

class Comp7TankCarousel(BattlePassTankCarousel):

    def __init__(self):
        super(Comp7TankCarousel, self).__init__()
        self._carouselDPCls = Comp7CarouselDataProvider
        self._carouselFilterCls = Comp7CarouselFilter

    def _getInitialFilterVO(self, contexts):
        filtersVO = super(Comp7TankCarousel, self)._getInitialFilterVO(contexts)
        filtersVO['isComp7'] = True
        return filtersVO

    def _getFilters(self):
        return super(Comp7TankCarousel, self)._getFilters() + ('comp7', )