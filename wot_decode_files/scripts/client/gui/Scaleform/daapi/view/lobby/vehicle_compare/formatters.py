# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/formatters.py
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.game_control.veh_comparison_basket import isValidVehicleForComparing
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IVehicleComparisonBasket

def packHeaderColumnData(columnID, btnWidth, btnHeight, label='', icon='', tooltip='', direction='descending', showSeparator=True, textAlign='center', enabled=False, verticalTextAlign='bottom'):
    return {'id': columnID, 
       'label': _ms(label), 
       'iconSource': icon, 
       'buttonWidth': btnWidth, 
       'toolTip': tooltip, 
       'defaultSortDirection': direction, 
       'buttonHeight': btnHeight, 
       'showSeparator': showSeparator, 
       'enabled': enabled, 
       'textAlign': textAlign, 
       'verticalTextAlign': verticalTextAlign}


def getTreeNodeCompareData(vehicle):
    comparisonBasket = dependency.instance(IVehicleComparisonBasket)
    return {'modeAvailable': comparisonBasket.isEnabled(), 
       'cmpBasketFull': not comparisonBasket.isReadyToAdd(vehicle)}


def resolveStateTooltip(comparisonBasket, vehicle, enabledTooltip, fullTooltip, invalidTooltip=VEH_COMPARE.VEHPREVIEW_COMPAREVEHICLEBTN_TOOLTIPS_CANNOTADDTOCOMPARE, miniclientTooltip=VEH_COMPARE.COMPAREVEHICLEBTN_TOOLTIPS_MINICLIENT):
    if not comparisonBasket.isAvailable():
        state, tooltip = False, miniclientTooltip
    elif comparisonBasket.isFull():
        state, tooltip = False, fullTooltip
    elif not isValidVehicleForComparing(vehicle):
        state, tooltip = False, invalidTooltip
    else:
        state, tooltip = True, enabledTooltip
    return (state, tooltip)