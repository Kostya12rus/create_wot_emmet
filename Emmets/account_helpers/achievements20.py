# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/achievements20.py
from functools import partial
import typing, AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, Optional

class Achievements20(object):

    def __init__(self, syncData, commandsProxy):
        self.__cache = {}
        self.__ignore = True
        self.__syncData = syncData
        self.__commandsProxy = commandsProxy
        self.__account = None
        return

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

    def setAccount(self, account):
        self.__account = account

    def synchronize(self, isFullSync, diff):
        if isFullSync and self.__cache:
            self.__cache.clear()
        if 'achievements20' in diff:
            synchronizeDicts(diff['achievements20'], self.__cache.setdefault('achievements20', {}))

    def setAchievementsLayout(self, layout, callback):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.CMD_SET_ACHIEVEMENTS20_LAYOUT, None)
            return
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr, ext)
        else:
            proxy = None
        self.__account._doCmdIntArr(AccountCommands.CMD_SET_ACHIEVEMENTS20_LAYOUT, layout, proxy)
        return

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return