# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/inventory_update_helper.py
from gui.shared.gui_items import GUI_ITEM_TYPE

def updateOnInventoryChanges(itemsCache, vehicle, invDiff):
    isNeedToUpdate = True
    if invDiff is not None and GUI_ITEM_TYPE.TANKMAN in invDiff:
        diff = invDiff[GUI_ITEM_TYPE.TANKMAN]
        if 'compDescr' in diff:
            invIDs = diff['compDescr']
            for tankmanInvID in invIDs.iterkeys():
                tankman = itemsCache.items.getTankman(tankmanInvID)
                if tankman and tankman.isInTank and tankman.vehicleInvID == vehicle.invID:
                    isNeedToUpdate = True
                    break
                else:
                    isNeedToUpdate = False

    return isNeedToUpdate