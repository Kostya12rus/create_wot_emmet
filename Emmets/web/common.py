# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/common.py
import typing
from helpers import dependency
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