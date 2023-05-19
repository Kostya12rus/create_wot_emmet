# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/spa_flags.py
from external_strings_utils import strtobool, InvalidStringValueException
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from constants import SPA_ATTRS

class SPAFlags(object):

    def __init__(self, syncData):
        super(SPAFlags, self).__init__()
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

    def synchronize(self, diff):
        cacheDiff = diff.get('cache', None)
        spaCache = cacheDiff.get('SPA', None) if cacheDiff else None
        itemDiff = {}
        if spaCache:
            for key in SPA_ATTRS.toClientAttrs():
                value = spaCache.get(key, None)
                if value:
                    try:
                        itemDiff[key] = strtobool(value)
                    except InvalidStringValueException:
                        itemDiff[key] = value

        synchronizeDicts(itemDiff, self.__cache.setdefault('spaFlags', {}))
        return

    def getFlag(self, flagName):
        if self.__cache and 'spaFlags' in self.__cache:
            return self.__cache['spaFlags'].get(flagName, None)
        else:
            return