# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/post_progression_prices_common.py
from items import vehicles

def getPostProgressionPrice(priceTag, vehType, priceContainer=None):
    postProgressionPricesOverrides = vehType.postProgressionPricesOverrides
    postProgressionPrices = priceContainer if priceContainer else vehicles.g_cache.postProgression().prices
    if postProgressionPricesOverrides and priceTag in postProgressionPricesOverrides:
        price = postProgressionPricesOverrides[priceTag]
    else:
        price = postProgressionPrices.get(priceTag, {}).get(vehType.level, {})
    return price