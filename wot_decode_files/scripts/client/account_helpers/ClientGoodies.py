# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/ClientGoodies.py
from functools import partial
import AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts

class ClientGoodies(object):

    def __init__(self, syncData):
        self.__account = None
        self.__syncData = syncData
        self.__cache = {}
        self.__ignore = True
        return

    def onAccountBecomePlayer(self):
        self.__ignore = False

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True

    def setAccount(self, account):
        self.__account = account

    def synchronize(self, isFullSync, diff):
        if isFullSync:
            self.__cache.clear()
        goodiesFull = diff.get(('goodies', '_r'))
        if goodiesFull:
            self.__cache = dict(goodiesFull)
        goodiesDiff = diff.get('goodies', None)
        if goodiesDiff is not None:
            synchronizeDicts(goodiesDiff, self.__cache.setdefault('goodies', {}))
        if 'cache' in diff:
            clanReservesDiff = diff['cache'].get('activeOrders', {})
            synchronizeDicts(clanReservesDiff, self.__cache.setdefault('clanReserves', {}))
        pr2ConversionResult = diff.get('pr2_conversion')
        if pr2ConversionResult is not None:
            self.__cache['pr2_conversion'] = pr2ConversionResult
        return

    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        return

    def getItems(self, itemsType, callback):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetItemsResponse, itemsType, callback))
        return

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return

    def __onGetItemsResponse(self, itemsType, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache.get(itemsType, None))
        return