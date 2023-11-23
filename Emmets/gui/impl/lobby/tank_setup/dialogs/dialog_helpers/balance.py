# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/dialogs/dialog_helpers/balance.py
from frameworks.wulf.view.array import fillViewModelsArray
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sub_views.current_balance_model import CurrentBalanceModel

def initBalance(balanceArray, currencies, itemsCache):
    money = itemsCache.items.stats.money
    currencyModelsList = []
    for currency in currencies:
        cur = CurrentBalanceModel()
        cur.setCurrencyType(currency)
        cur.setCurrencyValue(money.get(currency, 0))
        currencyModelsList.append(cur)

    fillViewModelsArray(currencyModelsList, balanceArray)