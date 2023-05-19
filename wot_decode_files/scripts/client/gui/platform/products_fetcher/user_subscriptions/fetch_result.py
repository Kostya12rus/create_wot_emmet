# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/products_fetcher/user_subscriptions/fetch_result.py
from gui.platform.products_fetcher.fetch_result import FetchResult, ResponseStatus

class UserSubscriptionFetchResult(FetchResult):
    _CACHE_TTL = 300

    def stop(self):
        self._clearTimeoutBwCbId()
        self.status = ResponseStatus.UNDEFINED
        self.products = []