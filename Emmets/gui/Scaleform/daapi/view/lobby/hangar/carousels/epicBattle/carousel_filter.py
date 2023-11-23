# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/epicBattle/carousel_filter.py
from account_helpers.AccountSettings import EPICBATTLE_CAROUSEL_FILTER_1, EPICBATTLE_CAROUSEL_FILTER_2, EPICBATTLE_CAROUSEL_FILTER_CLIENT_1, EPICBATTLE_CAROUSEL_FILTER_CLIENT_2
from account_helpers.AccountSettings import AccountSettings
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import CarouselFilter
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from gui.Scaleform.daapi.view.battle.epic.battle_carousel_filters import FLRentedCriteriesGroup

class EpicBattleCarouselFilter(CarouselFilter):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)
    FILTER_KEY_SEASON = 'epicBattleSeason'

    def __init__(self):
        super(EpicBattleCarouselFilter, self).__init__()
        clientFilter = EPICBATTLE_CAROUSEL_FILTER_CLIENT_1 if self.__epicController.isUnlockVehiclesInBattleEnabled() else EPICBATTLE_CAROUSEL_FILTER_CLIENT_2
        self._serverSections = (
         EPICBATTLE_CAROUSEL_FILTER_1, EPICBATTLE_CAROUSEL_FILTER_2)
        self._clientSections = (clientFilter,)

    def save(self):
        self._filters[self.FILTER_KEY_SEASON] = self.__epicController.getCurrentSeasonID()
        super(EpicBattleCarouselFilter, self).save()

    def load(self):
        super(EpicBattleCarouselFilter, self).load()
        currentSeason = self.__epicController.getCurrentSeasonID()
        lastSeason = self._filters.get(self.FILTER_KEY_SEASON, currentSeason)
        if lastSeason != currentSeason:
            self.reset(save=False)

    def isDefault(self, keys=None):
        defaultFilters = AccountSettings.getFilterDefaults(self._serverSections)
        for section in self._clientSections:
            defaultFilters.update(AccountSettings.getFilterDefault(section))

        if keys is None:
            keys = defaultFilters.keys()
        for key in keys:
            if key != self.FILTER_KEY_SEASON and self._filters[key] != defaultFilters[key]:
                return False

        return True

    def _setCriteriaGroups(self):
        self._criteriesGroups = (
         FLRentedCriteriesGroup(),)