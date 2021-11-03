# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/epicBattle/carousel_filter.py
from account_helpers.AccountSettings import EPICBATTLE_CAROUSEL_FILTER_1, EPICBATTLE_CAROUSEL_FILTER_2, EPICBATTLE_CAROUSEL_FILTER_CLIENT_1, EPICBATTLE_CAROUSEL_FILTER_CLIENT_2
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import CarouselFilter
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

class EpicBattleCarouselFilter(CarouselFilter):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    def __init__(self):
        super(EpicBattleCarouselFilter, self).__init__()
        clientFilter = EPICBATTLE_CAROUSEL_FILTER_CLIENT_1 if self.__epicController.isUnlockVehiclesInBattleEnabled() else EPICBATTLE_CAROUSEL_FILTER_CLIENT_2
        self._serverSections = (
         EPICBATTLE_CAROUSEL_FILTER_1, EPICBATTLE_CAROUSEL_FILTER_2)
        self._clientSections = (clientFilter,)