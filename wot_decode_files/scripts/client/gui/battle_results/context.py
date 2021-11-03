# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/context.py
from constants import ARENA_BONUS_TYPE
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.simple(('getArenaUniqueID', 'arenaUniqueID'), ('needToShowImmediately',
                                                             'showImmediately'), ('needToShowIfPosted',
                                                                                  'showIfPosted'), ('resetCache',
                                                                                                    'resetCache'))
class RequestResultsContext(object):
    __slots__ = ('__arenaUniqueID', '__showImmediately', '__showIfPosted', '__resetCache',
                 '__arenaBonusType')

    def __init__(self, arenaUniqueID, arenaBonusType=ARENA_BONUS_TYPE.UNKNOWN, showImmediately=True, showIfPosted=False, resetCache=False):
        super(RequestResultsContext, self).__init__()
        self.__arenaUniqueID = arenaUniqueID
        self.__arenaBonusType = arenaBonusType
        self.__showImmediately = showImmediately
        self.__showIfPosted = showIfPosted
        self.__resetCache = resetCache

    def getArenaUniqueID(self):
        return self.__arenaUniqueID

    def getArenaBonusType(self):
        return self.__arenaBonusType

    def needToShowImmediately(self):
        return self.__showImmediately and self.__arenaBonusType not in ARENA_BONUS_TYPE.BATTLE_ROYALE_RANGE and self.__arenaBonusType not in (ARENA_BONUS_TYPE.MAPS_TRAINING, ARENA_BONUS_TYPE.EVENT_BATTLES)

    def needToShowIfPosted(self):
        return self.__showIfPosted

    def resetCache(self):
        return self.__resetCache


@ReprInjector.simple(('getEmblemType', 'type'), ('getUniqueID', 'ids'))
class RequestEmblemContext(object):
    __slots__ = ('__emblemType', '__formationDBID', '__textureID')

    def __init__(self, emblemType, formationDBID, textureID=0):
        super(RequestEmblemContext, self).__init__()
        self.__emblemType = emblemType
        self.__formationDBID = formationDBID
        self.__textureID = textureID

    def getEmblemType(self):
        return self.__emblemType

    def getFormationDBID(self):
        return self.__formationDBID

    def getTextureID(self):
        return self.__textureID

    def getUniqueID(self):
        return (
         self.getEmblemType(), self.__formationDBID)