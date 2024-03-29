# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/badges/BadgesCollector.py
import operator
from collections import defaultdict
import typing
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.badge import Badge

class BadgesCollector(object):

    def __init__(self):
        self.__receivedBadges = []
        self.__notReceivedBadges = []
        self.__suffixBadges = []

    def getReceivedPrefixBadges(self):
        return tuple(self.__receivedBadges)

    def getNotReceivedPrefixBadges(self):
        return tuple(self.__notReceivedBadges)

    def getSuffixAchievedBadges(self):
        return tuple(self.__suffixBadges)

    def updateCollector(self, badges=None):
        if badges is not None:
            self.__clear()
            self.__preprocessBadges(badges)
        return

    def __isReceivedPrefixBadges(self, badge):
        return badge.isPrefixLayout() and badge.isAchieved

    def __isNotReceivedPrefixBadges(self, badge):
        return badge.isPrefixLayout() and not badge.isAchieved and badge.isVisibleAsAchievable() and not badge.isObsolete()

    def __isSuffixAchivedBadge(self, badge):
        return badge.isSuffixLayout() and badge.isAchieved

    def __clear(self):
        self.__receivedBadges = []
        self.__notReceivedBadges = []
        self.__suffixBadges = []

    def __preprocessBadges(self, badges):
        cache = defaultdict(list)
        for badge in badges:
            if self.__isSuffixAchivedBadge(badge):
                self.__suffixBadges.append(badge)
            elif badge.isCollapsible():
                cache[badge.group].append(badge)
            elif self.__isNotReceivedPrefixBadges(badge):
                self.__notReceivedBadges.append(badge)
            elif self.__isReceivedPrefixBadges(badge):
                self.__receivedBadges.append(badge)

        for cachedBadges in cache.itervalues():
            byClass = sorted(cachedBadges, key=operator.methodcaller('getBadgeClass'), reverse=True)
            for cachedBadge in byClass:
                if self.__isNotReceivedPrefixBadges(cachedBadge):
                    self.__notReceivedBadges.append(cachedBadge)
                elif self.__isReceivedPrefixBadges(cachedBadge):
                    self.__receivedBadges.append(cachedBadge)
                    break

        self.__suffixBadges.sort()
        self.__notReceivedBadges.sort()
        self.__receivedBadges.sort()