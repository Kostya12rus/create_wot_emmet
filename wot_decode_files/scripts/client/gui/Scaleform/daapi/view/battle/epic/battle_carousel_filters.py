# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic/battle_carousel_filters.py
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import RoleCriteriesGroup
from gui.shared.utils.requesters.ItemsRequester import RequestCriteria, PredicateCondition
FL_RENT = RequestCriteria(PredicateCondition((lambda item: item.name.endswith('_FL'))))

class FLRentedCriteriesGroup(RoleCriteriesGroup):

    def update(self, filters):
        super(FLRentedCriteriesGroup, self).update(filters)
        if not filters['rented']:
            self._criteria |= ~FL_RENT

    @staticmethod
    def isApplicableFor(vehicle):
        return True