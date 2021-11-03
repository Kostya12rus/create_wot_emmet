# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/festivity_manager.py
import logging
from functools import partial
import AccountCommands
from helpers import dependency
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from skeletons.festivity_factory import IFestivityFactory
_logger = logging.getLogger()

class FestivityManager(object):
    _festivityFactory = dependency.descriptor(IFestivityFactory)

    def __init__(self, syncData, clientCommandsProxy):
        self.__syncData = syncData
        self.__cache = {}
        self.__ignore = True
        self.__festivityKey = self._festivityFactory.getRequester().dataKey
        self._festivityFactory.getProcessor().setCommandProxy(clientCommandsProxy)

    def onAccountBecomePlayer(self):
        self.__ignore = False

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True

    def setAccount(self, account):
        self._festivityFactory.getProcessor().setAccount(account)

    def synchronize(self, isFullSync, diff):
        if isFullSync:
            self.__cache.clear()
        itemDiff = diff.get(self.__festivityKey, None)
        _logger.debug('Syncing cache for key %s: %s', self.__festivityKey, itemDiff)
        if itemDiff is not None:
            synchronizeDicts(itemDiff, self.__cache.setdefault(self.__festivityKey, {}))
        return

    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        return

    def get(self, itemName, callback):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetResponse, itemName, callback))
        return

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return

    def __onGetResponse(self, itemName, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache[self.__festivityKey].get(itemName, None))
        return