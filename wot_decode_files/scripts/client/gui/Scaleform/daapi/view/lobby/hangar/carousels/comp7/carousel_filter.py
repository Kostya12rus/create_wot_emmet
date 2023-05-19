# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/comp7/carousel_filter.py
from account_helpers.AccountSettings import COMP7_CAROUSEL_FILTER_1, COMP7_CAROUSEL_FILTER_2, COMP7_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_filter import BattlePassCarouselFilter, BattlePassCriteriesGroup
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import EventCriteriesGroup
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7CarouselFilter(BattlePassCarouselFilter):

    def __init__(self):
        super(Comp7CarouselFilter, self).__init__()
        self._serverSections = (COMP7_CAROUSEL_FILTER_1, COMP7_CAROUSEL_FILTER_2, BATTLEPASS_CAROUSEL_FILTER_1)
        self._clientSections = (COMP7_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1)
        self._criteriesGroups = (
         EventCriteriesGroup(), Comp7CriteriesGroup())


class Comp7CriteriesGroup(BattlePassCriteriesGroup):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def update(self, filters):
        super(Comp7CriteriesGroup, self).update(filters)
        if filters.get('comp7'):
            self._criteria |= REQ_CRITERIA.CUSTOM(self._comp7Criteria)

    @classmethod
    def _comp7Criteria(cls, vehicle):
        return cls.__comp7Controller.isSuitableVehicle(vehicle) is None