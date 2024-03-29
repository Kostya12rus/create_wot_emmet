# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCTankCarousel.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels import TankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_data_provider import BCCarouselDataProvider
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import CarouselFilter, CriteriesGroup

class BCCriteriesGroup(CriteriesGroup):

    def apply(self, vehicle):
        return True

    @staticmethod
    def isApplicableFor(vehicle):
        return True


class BCCarouselFilter(CarouselFilter):

    def __init__(self):
        super(BCCarouselFilter, self).__init__()
        self._criteriesGroups = (BCCriteriesGroup(),)

    def load(self):
        pass

    def isDefault(self, keys=None):
        return True

    def getFilters(self, keys=None):
        return {}


class BCTankCarousel(TankCarousel):

    def __init__(self):
        super(BCTankCarousel, self).__init__()
        self._carouselDPCls = BCCarouselDataProvider
        self._carouselFilterCls = BCCarouselFilter
        self._usedFilters = ()

    def _getFiltersVisible(self):
        return False

    def updateParams(self):
        pass

    def hasRoles(self):
        return False