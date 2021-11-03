# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/shop/stats.py
from skeletons.gui.game_control import IWalletController
from web.client_web_api.api import C2WHandler, c2w
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.game_control.wallet import WalletController
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class BalanceEventHandler(C2WHandler):
    __walletController = dependency.descriptor(IWalletController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def init(self):
        super(BalanceEventHandler, self).init()
        self.__walletController.onWalletStatusChanged += self.__onWalletUpdate
        g_clientUpdateManager.addCallbacks({('stats.{}').format(c):self.__onBalanceUpdate for c in Currency.ALL})

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self, force=True)
        self.__walletController.onWalletStatusChanged -= self.__onWalletUpdate
        super(BalanceEventHandler, self).fini()

    @c2w(name='balance_update')
    def __onBalanceUpdate(self, *_):
        stats = self.__itemsCache.items.stats
        actualMoney = stats.actualMoney.toDict()
        balanceData = {Currency.currencyExternalName(currency):actualMoney[currency] for currency in Currency.ALL if currency in actualMoney}
        return balanceData

    @c2w(name='wallet_update')
    def __onWalletUpdate(self, *_):
        stats = self.__itemsCache.items.stats
        return {Currency.currencyExternalName(key):WalletController.STATUS.getKeyByValue(code).lower() for key, code in stats.currencyStatuses.items() if key in Currency.ALL if key in Currency.ALL}