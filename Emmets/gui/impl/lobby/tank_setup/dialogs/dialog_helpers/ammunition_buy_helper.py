# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/dialogs/dialog_helpers/ammunition_buy_helper.py
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