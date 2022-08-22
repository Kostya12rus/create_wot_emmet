# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/trade_in_common/constants_types.py
from collections import namedtuple
CONFIG_NAME = 'trade_in_config'
ConversionRule = namedtuple('ConversionRule', [
 'freeExchange', 'sellPriceFactor', 'accessToken', 'checkVehicleAscendingLevels',
 'visibleToEveryone', 'allowToBuyNotInShopVehicles'])
TradeInInfo = namedtuple('TradeInInfo', ['sellGroupId', 'buyGroupId', 'conversionRule'])