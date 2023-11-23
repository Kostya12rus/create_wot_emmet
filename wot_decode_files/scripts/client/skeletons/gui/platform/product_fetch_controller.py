# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/platform/product_fetch_controller.py
from typing import TYPE_CHECKING
from skeletons.gui.platform.controller import IPlatformRequestController
if TYPE_CHECKING:
    from gui.platform.products_fetcher.fetch_result import FetchResult

class IProductFetchController(IPlatformRequestController):

    def getProducts(self, showWaiting=True):
        raise NotImplementedError


class ISubscriptionProductsFetchController(IProductFetchController):
    pass


class IUserSubscriptionsFetchController(IPlatformRequestController):
    pass