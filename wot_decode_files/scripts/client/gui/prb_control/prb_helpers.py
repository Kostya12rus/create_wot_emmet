# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/prb_helpers.py
import logging
from gui.shared.badges import buildBadge
from gui.shared.gui_items.badge import BadgeLayouts
from helpers import dependency
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def _findFirstPrefixBadge(selectedBadges, itemsCache=None):
    badgeDescrs = itemsCache.items.badges.available
    if not isinstance(selectedBadges, (tuple, list)):
        if isinstance(selectedBadges, int):
            return selectedBadges
        return 0
    for sbID in selectedBadges:
        badgeDescr = badgeDescrs.get(sbID)
        if badgeDescr and badgeDescr['layout'] == BadgeLayouts.PREFIX:
            return sbID

    return 0


class BadgesHelper(object):

    def __init__(self, badges=None):
        if isinstance(badges, (list, tuple)) and badges and not isinstance(badges[0], (list, tuple)):
            _logger.error('Converting badges data %s', badges)
            self.__badgesRawData = (badges, [])
        else:
            self.__badgesRawData = badges or ([], [])
        self.__badges = {}
        self.__prefixBadgeID = None
        return

    def getBadge(self):
        badgeID = self.__getBadgeID()
        if badgeID <= 0:
            return None
        else:
            if badgeID not in self.__badges:
                self.__badges[badgeID] = buildBadge(badgeID, self.__getBadgeExtraInfo())
            return self.__badges[badgeID]

    def __getBadgeID(self):
        if self.__prefixBadgeID is None:
            self.__prefixBadgeID = _findFirstPrefixBadge(self.__getSelectedBadges())
        return self.__prefixBadgeID

    def __getSelectedBadges(self):
        if not self.__badgesRawData:
            _logger.error('Invalid selected badge data')
            return []
        return self.__badgesRawData[0]

    def __getBadgeExtraInfo(self):
        if len(self.__badgesRawData) < 2:
            _logger.error('Invalid badge data %s', self.__badgesRawData)
            return None
        else:
            return self.__badgesRawData[1]