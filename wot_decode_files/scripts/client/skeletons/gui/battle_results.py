# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/battle_results.py
from Event import Event

class IBattleResultsService(object):
    __slots__ = ()
    onResultPosted = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def requestResults(self, ctx, callback=None):
        raise NotImplementedError

    def requestEmblem(self, ctx, callback=None):
        raise NotImplementedError

    def postResult(self, result, needToShowUI=True):
        raise NotImplementedError

    def areResultsPosted(self, arenaUniqueID):
        raise NotImplementedError

    def getResultsVO(self, arenaUniqueID):
        raise NotImplementedError

    def popResultsAnimation(self, arenaUniqueID):
        raise NotImplementedError

    def saveStatsSorting(self, bonusType, iconType, sortDirection):
        raise NotImplementedError

    def applyAdditionalBonus(self, arenaUniqueID):
        raise NotImplementedError

    def isAddXPBonusApplied(self, arenaUniqueID):
        raise NotImplementedError

    def isAddXPBonusEnabled(self, arenaUniqueID):
        raise NotImplementedError

    def getAdditionalXPValue(self, arenaUniqueID):
        raise NotImplementedError

    def isCrewSameForArena(self, arenaUniqueID):
        raise NotImplementedError

    def isXPToTManSameForArena(self, arenaUniqueID):
        raise NotImplementedError

    def getVehicleForArena(self, arenaUniqueID):
        raise NotImplementedError