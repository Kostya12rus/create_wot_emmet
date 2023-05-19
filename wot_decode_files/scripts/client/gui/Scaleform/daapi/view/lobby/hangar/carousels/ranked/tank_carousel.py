# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/ranked/tank_carousel.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels.ranked.carousel_data_provider import RankedCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.ranked.carousel_filter import RankedCarouselFilter
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.tank_carousel import BattlePassTankCarousel

class RankedTankCarousel(BattlePassTankCarousel):

    def __init__(self):
        super(RankedTankCarousel, self).__init__()
        self._carouselDPCls = RankedCarouselDataProvider
        self._carouselFilterCls = RankedCarouselFilter

    def _getInitialFilterVO(self, contexts):
        filtersVO = super(RankedTankCarousel, self)._getInitialFilterVO(contexts)
        filtersVO['isRanked'] = True
        return filtersVO

    def _getFilters(self):
        return super(RankedTankCarousel, self)._getFilters() + ('ranked', )