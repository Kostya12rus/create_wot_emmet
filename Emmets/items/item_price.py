# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/item_price.py
from goodies.GoodieResources import Gold, Credits

class PRICE_TYPE:
    DEFAULT = (0, )
    PROMO = (1, )
    PERSONAL = (2, )


def getItemPrice(item, gameParams, goodies=None, goodieTarget=None):
    priceType = PRICE_TYPE.DEFAULT
    actualPrice = gameParams['items']['itemPrices'][item]
    defaultPrice = gameParams['defaults'].get('items', {}).get('itemPrices', {}).get(item, None)
    if not defaultPrice:
        defaultPrice = actualPrice
    else:
        priceType = PRICE_TYPE.PROMO
    if (actualPrice[0] == 0 or actualPrice[1] == 0) and goodies and goodieTarget:
        personalDiscounts = goodies.test(goodieTarget, {Credits(defaultPrice[0]), Gold(defaultPrice[1])})
        for _, discount in personalDiscounts.iteritems():
            if isinstance(discount, Gold) and discount.value <= actualPrice[1]:
                actualPrice = (
                 0, discount.value)
                priceType = PRICE_TYPE.PERSONAL
            elif isinstance(discount, Credits) and discount.value <= actualPrice[0]:
                actualPrice = (
                 discount.value, 0)
                priceType = PRICE_TYPE.PERSONAL

    return (
     defaultPrice, actualPrice, priceType)


def getNextSlotPrice(slots, slotsPrices):
    addSlotNumber = slots - slotsPrices[0]
    if addSlotNumber < 0:
        if len(slotsPrices[1]):
            return (slotsPrices[1][0][0], 0)
        return ('credits', 0)
    if addSlotNumber < len(slotsPrices[1]):
        return slotsPrices[1][addSlotNumber]
    return slotsPrices[1][-1]


def getNextBerthPackPrice(berths, berthsPrices):
    addPackNumber = (berths - berthsPrices[0]) / berthsPrices[1]
    if addPackNumber < 0:
        return 0
    if addPackNumber < len(berthsPrices[2]):
        return berthsPrices[2][addPackNumber]
    return berthsPrices[2][-1]