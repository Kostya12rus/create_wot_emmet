# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/products_fetcher/__init__.py
import typing
from gui.platform.products_fetcher.subscriptions.subscriptions_controller import SubscriptionFetcherController
from gui.platform.products_fetcher.user_subscriptions.controller import UserSubscriptionsFetchController
from skeletons.gui.platform.product_fetch_controller import ISubscriptionsFetchController, IUserSubscriptionsFetchController
if typing.TYPE_CHECKING:
    from helpers.dependency import DependencyManager
__all__ = ('getProductFetchControllers', )

def getProductFetchControllers(manager):
    subscriptionsFetchController = SubscriptionFetcherController()
    subscriptionsFetchController.init()
    manager.addInstance(ISubscriptionsFetchController, subscriptionsFetchController, finalizer='fini')
    userSubscriptionsFetchController = UserSubscriptionsFetchController()
    userSubscriptionsFetchController.init()
    manager.addInstance(IUserSubscriptionsFetchController, userSubscriptionsFetchController, finalizer='fini')