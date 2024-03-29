# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_post_progression/vo_builders/base_page_vos.py
import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles, getRoleTextWithIcon
from gui.shared.gui_items.Vehicle import getNationLessName, getIconResourceName
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

def getBaseButtonsVO(vehicle):
    iconName = getIconResourceName(getNationLessName(vehicle.name))
    return {'shopIconPath': backport.image(R.images.gui.maps.shop.vehicles.c_360x270.dyn(iconName)()), 
       'compareBtnVisible': True, 
       'goToVehicleViewBtnVisible': True, 
       'isPremium': vehicle.isPremium or vehicle.buyPrices.itemPrice.isActionPrice(), 
       'vehicleId': vehicle.intCD}


def getBaseDataVO(vehicle):
    return {'showDemountAllPairsBtn': False, 
       'showExpBlock': False, 
       'vehicleButton': {}, 'vehicleInfo': {}, 'nation': vehicle.nationName}


def getBaseTitleVO(vehicle):
    tankUserName = vehicle.userName
    return {'intCD': vehicle.intCD, 
       'tankNameStr': text_styles.grandTitle(tankUserName), 
       'tankNameStrSmall': text_styles.promoTitle(tankUserName), 
       'statusStr': '', 
       'roleText': getRoleTextWithIcon(vehicle.role, vehicle.roleLabel), 
       'showInfoIcon': False}