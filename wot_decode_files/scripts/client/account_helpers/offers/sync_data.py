# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/offers/sync_data.py
from account_helpers.AccountSyncData import BaseSyncDataCache
from shared_utils.account_helpers.diff_utils import synchronizeDicts

class OffersSyncData(BaseSyncDataCache):

    def _synchronize(self, diff):
        itemDiff = diff.get('offersData')
        if itemDiff is not None:
            synchronizeDicts(itemDiff, self._cache.setdefault('offersData', {}))
        return