# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/game_restrictions.py
import logging
from functools import partial
import AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts
_logger = logging.getLogger(__name__)
_CACHE_DIFF_KEY = 'cache'
_GAME_RESTRICTIONS_KEY = 'gameRestrictions'

class GameRestrictions(object):

    def __init__(self, syncData):
        super(GameRestrictions, self).__init__()
        self.__syncData = syncData
        self.__cache = {}
        self.__ignore = True

    def onAccountBecomePlayer(self):
        self.__ignore = False

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True

    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        return

    def synchronize(self, isFullSync, diff):
        _logger.debug('Synchronize game restrictions')
        if isFullSync and self.__cache:
            self.__cache.clear()
        if _CACHE_DIFF_KEY in diff and _GAME_RESTRICTIONS_KEY in diff[_CACHE_DIFF_KEY]:
            synchronizeDicts(diff[_CACHE_DIFF_KEY][_GAME_RESTRICTIONS_KEY], self.__cache)
        _logger.debug('Game restrictions info: %s', self.__cache)

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return