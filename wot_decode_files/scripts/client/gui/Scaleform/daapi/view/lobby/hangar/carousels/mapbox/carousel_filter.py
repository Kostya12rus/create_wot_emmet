# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/mapbox/carousel_filter.py
from account_helpers.AccountSettings import MAPBOX_CAROUSEL_FILTER_1, MAPBOX_CAROUSEL_FILTER_2, MAPBOX_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_filter import BattlePassCarouselFilter

class MapboxCarouselFilter(BattlePassCarouselFilter):

    def __init__(self):
        super(MapboxCarouselFilter, self).__init__()
        self._serverSections = (MAPBOX_CAROUSEL_FILTER_1, MAPBOX_CAROUSEL_FILTER_2, BATTLEPASS_CAROUSEL_FILTER_1)
        self._clientSections = (MAPBOX_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1)