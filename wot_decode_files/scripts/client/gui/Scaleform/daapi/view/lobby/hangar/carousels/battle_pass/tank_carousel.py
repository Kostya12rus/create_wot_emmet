# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/battle_pass/tank_carousel.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_data_provider import BattlePassCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_filter import BattlePassCarouselFilter
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController

class BattlePassTankCarousel(TankCarousel):
    _battlePassController = dependency.descriptor(IBattlePassController)

    def __init__(self):
        super(BattlePassTankCarousel, self).__init__()
        self._carouselDPCls = BattlePassCarouselDataProvider
        self._carouselFilterCls = BattlePassCarouselFilter

    def _getInitialFilterVO(self, contexts):
        filtersVO = super(BattlePassTankCarousel, self)._getInitialFilterVO(contexts)
        filtersVO.update({'popoverAlias': VIEW_ALIAS.BATTLEPASS_CAROUSEL_FILTER_POPOVER})
        return filtersVO

    def _populate(self):
        super(BattlePassTankCarousel, self)._populate()
        self._battlePassController.onPointsUpdated += self.__onPointsUpdated
        self._battlePassController.onBattlePassSettingsChange += self.__onServerSettingChanged
        self.app.loaderManager.onViewLoaded += self.__onViewLoaded

    def _dispose(self):
        self._battlePassController.onPointsUpdated -= self.__onPointsUpdated
        self._battlePassController.onBattlePassSettingsChange -= self.__onServerSettingChanged
        self.app.loaderManager.onViewLoaded -= self.__onViewLoaded
        super(BattlePassTankCarousel, self)._dispose()

    def __onPointsUpdated(self):
        self.updateVehicles()

    def __onViewLoaded(self, view, *args, **kwargs):
        if view.alias == VIEW_ALIAS.BATTLEPASS_CAROUSEL_FILTER_POPOVER:
            view.setTankCarousel(self)

    def __onServerSettingChanged(self, *_):
        self.updateVehicles()
        self.__updateFilter()

    def __updateFilter(self):
        carouselFilter = self._carouselDPConfig.get('carouselFilter', None)
        if carouselFilter is not None:
            if carouselFilter.currentSeasonID != self._battlePassController.getSeasonID():
                carouselFilter.currentSeasonID = self._battlePassController.getSeasonID()
                carouselFilter.save()
        return