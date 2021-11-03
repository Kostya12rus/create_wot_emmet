# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/royale/carousel_filter.py
from account_helpers.AccountSettings import ROYALE_CAROUSEL_FILTER_1, ROYALE_CAROUSEL_FILTER_2, ROYALE_CAROUSEL_FILTER_CLIENT_1
from gui.Scaleform.daapi.view.common.vehicle_carousel import carousel_filter

class RoyaleCarouselFilter(carousel_filter.CarouselFilter):

    def __init__(self):
        super(RoyaleCarouselFilter, self).__init__()
        self._serverSections = (ROYALE_CAROUSEL_FILTER_1, ROYALE_CAROUSEL_FILTER_2)
        self._clientSections = (ROYALE_CAROUSEL_FILTER_CLIENT_1,)

    def _setCriteriaGroups(self):
        self._criteriesGroups = (
         carousel_filter.EventCriteriesGroup(),
         carousel_filter.BattleRoyaleCriteriesGroup())