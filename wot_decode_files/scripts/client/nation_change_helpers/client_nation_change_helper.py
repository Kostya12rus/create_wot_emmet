# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/nation_change_helpers/client_nation_change_helper.py
from CurrentVehicle import g_currentVehicle
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.utils.functions import makeTooltip
from helpers import dependency
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup, isMainInNationGroup
from skeletons.gui.shared import IItemsCache

def getValidVehicleCDForNationChange(vehCompDescr):
    tempVehCD = vehCompDescr
    vehicle = _getItem(vehCompDescr)
    if vehicle.hasNationGroup:
        if vehicle.isInInventory:
            if not vehicle.activeInNationGroup:
                tempVehCD = iterVehTypeCDsInNationGroup(vehCompDescr).next()
        elif not isMainInNationGroup(vehCompDescr):
            tempVehCD = iterVehTypeCDsInNationGroup(vehCompDescr).next()
    return tempVehCD


def getChangeNationTooltip():
    isChangeNationVisible = g_currentVehicle.isPresent() and g_currentVehicle.item.hasNationGroup
    isNationChangeAvailable = g_currentVehicle.isPresent() and g_currentVehicle.item.isNationChangeAvailable
    if isChangeNationVisible:
        if isNationChangeAvailable:
            changeNationTooltipHeader = R.strings.tooltips.hangar.nationChange.header()
            changeNationTooltipBody = R.strings.tooltips.hangar.nationChange.body()
        else:
            changeNationTooltipHeader = R.strings.tooltips.hangar.nationChange.disabled.header()
            if g_currentVehicle.item.isBroken:
                changeNationTooltipBody = R.strings.tooltips.hangar.nationChange.disabled.body.destroyed()
            elif g_currentVehicle.item.isInBattle:
                changeNationTooltipBody = R.strings.tooltips.hangar.nationChange.disabled.body.inBattle()
            elif g_currentVehicle.item.isInUnit:
                changeNationTooltipBody = R.strings.tooltips.hangar.nationChange.disabled.body.inSquad()
            else:
                changeNationTooltipBody = ''
        if changeNationTooltipBody == '':
            changeNationTooltip = makeTooltip(backport.text(changeNationTooltipHeader), '')
        else:
            changeNationTooltip = makeTooltip(backport.text(changeNationTooltipHeader), backport.text(changeNationTooltipBody))
    else:
        changeNationTooltip = ''
    return changeNationTooltip


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def _getItem(itemID, itemsCache=None):
    return itemsCache.items.getItemByCD(itemID)