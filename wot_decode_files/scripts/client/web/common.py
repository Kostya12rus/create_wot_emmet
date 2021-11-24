# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/common.py
import typing
from helpers import dependency
from gui.game_control.wallet import WalletController
from gui.shared.money import Currency
from skeletons.gui.shared.utils.requesters import IStatsRequester
from skeletons.gui.game_control import IShopSalesEventController as IShopSales
if typing.TYPE_CHECKING:
    from typing import Dict, Union
    from gui.shared.money import Money

@dependency.replace_none_kwargs(shopSales=IShopSales)
def formatShopSalesInfo(shopSales=None):
    return {'enabled': shopSales.isEnabled, 
       'dates': {'active': {'from': shopSales.activePhaseStartTime, 
                            'to': shopSales.activePhaseFinishTime}, 
                 'end': shopSales.eventFinishTime}, 
       'reroll': {'price': shopSales.reRollPrice.toSignDict()}, 
       'bundle': {'id': shopSales.currentBundleID, 
                  'rerolls': shopSales.currentBundleReRolls}}


def getBalance(stats):
    actualMoney = stats.actualMoney.toDict()
    balanceData = {Currency.currencyExternalName(currency):actualMoney.get(currency, 0) for currency in Currency.ALL}
    balanceData.update(stats.dynamicCurrencies)
    return balanceData


def getWalletCurrencyStatuses(stats):
    statuses = {Currency.currencyExternalName(currencyCode):WalletController.STATUS.getKeyByValue(statusCode).lower() for currencyCode, statusCode in stats.currencyStatuses.iteritems() if currencyCode in Currency.ALL if currencyCode in Currency.ALL}
    statuses.update({currencyCode:WalletController.STATUS.getKeyByValue(statusCode).lower() for currencyCode, statusCode in stats.dynamicCurrencyStatuses.iteritems()})
    return statuses