# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/goodies/demount_kit.py
from gui.goodies.goodie_items import DemountKit
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.shared import IItemsCache

def isDemountKitApplicableTo(optDevice):
    if optDevice.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE and not optDevice.isRemovable and optDevice.canUseDemountKit:
        demountKit, _ = getDemountKitForOptDevice(optDevice)
        return demountKit and demountKit.enabled
    return False


def getDemountKitForOptDevice(optDevice):
    itemsCache = dependency.instance(IItemsCache)
    goodiesCache = dependency.instance(IGoodiesCache)
    currency = optDevice.getRemovalPrice(itemsCache.items).getCurrency()
    demountKit = goodiesCache.getDemountKit(currency=currency)
    return (
     demountKit, currency)