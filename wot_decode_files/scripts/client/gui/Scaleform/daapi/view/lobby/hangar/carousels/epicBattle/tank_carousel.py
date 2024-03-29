# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/epicBattle/tank_carousel.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.epicBattle.carousel_data_provider import EpicBattleCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.epicBattle.carousel_filter import EpicBattleCarouselFilter
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

class EpicBattleTankCarousel(TankCarousel):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)
    _DISABLED_FILTERS = [
     'bonus']

    def __init__(self):
        super(EpicBattleTankCarousel, self).__init__()
        self._carouselDPCls = EpicBattleCarouselDataProvider
        self._carouselFilterCls = EpicBattleCarouselFilter

    def _populate(self):
        super(EpicBattleTankCarousel, self)._populate()
        self.as_useExtendedCarouselS(self.__epicController.isUnlockVehiclesInBattleEnabled())
        indexToScroll = self._carouselDP.getIndexToScroll()
        if indexToScroll >= 0:
            self.as_scrollToSlotS(indexToScroll)

    def _getInitialFilterVO(self, contexts):
        filtersVO = super(EpicBattleTankCarousel, self)._getInitialFilterVO(contexts)
        filtersVO['isFrontline'] = True
        for entry in filtersVO.get('hotFilters', []):
            if entry['id'] in self._DISABLED_FILTERS:
                entry['enabled'] = False
                entry['selected'] = False

        return filtersVO