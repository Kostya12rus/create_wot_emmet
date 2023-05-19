# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/ItemRestore.py


class RESTORE_VEHICLE_TYPE:
    PREMIUM = 0
    ACTION = 1


def getVehicleRestorePrice(defaultBuyPrice, exchangeRate, sellPriceFactor, sellToRestoreFactor):
    credits = defaultBuyPrice[0] + defaultBuyPrice[1] * exchangeRate
    return (int(credits * sellPriceFactor * sellToRestoreFactor), 0)


def getVehicleRestorePriceShort(vehTypeCompDescr, gameParams):
    if 'defaults' in gameParams and 'items' in gameParams['defaults'] and 'itemPrices' in gameParams['defaults']['items'] and vehTypeCompDescr in gameParams['defaults']['items']['itemPrices']:
        defaultBuyPrice = gameParams['defaults']['items']['itemPrices'][vehTypeCompDescr]
    else:
        defaultBuyPrice = gameParams['items']['itemPrices'][vehTypeCompDescr]
    exchangeRate = gameParams['economics']['exchangeRate']
    sellPriceFactor = gameParams['sellPriceFactor']
    sellToRestore = gameParams['restore_config']['vehicles']['sellToRestoreFactor']
    return getVehicleRestorePrice(defaultBuyPrice, exchangeRate, sellPriceFactor, sellToRestore)