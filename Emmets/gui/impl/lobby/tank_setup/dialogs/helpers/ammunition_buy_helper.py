# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/dialogs/helpers/ammunition_buy_helper.py
from gui.shared.gui_items import GUI_ITEM_TYPE
_MODULES_ORDER = (
 GUI_ITEM_TYPE.GUN,
 GUI_ITEM_TYPE.TURRET,
 GUI_ITEM_TYPE.ENGINE,
 GUI_ITEM_TYPE.CHASSIS,
 GUI_ITEM_TYPE.RADIO)

def _getModuleOrderByType(itemType):
    if itemType in GUI_ITEM_TYPE.VEHICLE_MODULES:
        return _MODULES_ORDER.index(itemType)
    return -1


def modulesSortFunction(i1, i2):
    return cmp(_getModuleOrderByType(i1.getTypeID()), _getModuleOrderByType(i2.getTypeID()))


def isFreeInstalling(item, vehicle):
    if vehicle is not None:
        return item.isInInventory or item.isInOtherLayout(vehicle)
    else:
        return item.isInInventory