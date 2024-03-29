# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/sales/commands.py
from account_helpers.AccountSettings import AccountSettings
from gui.Scaleform.daapi.view.lobby.store.browser import shop_helpers
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.server_events.events_dispatcher import showMissionsMarathon
from gui.shared import g_eventBus
from gui.shared.event_dispatcher import showShop
from gui.shared.events import OpenLinkEvent
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from helpers import dependency
from skeletons.gui.game_control import ICalendarController
from gui.game_control.calendar_controller import CalendarInvokeOrigin

def buySlots():
    ActionsFactory.doAction(ActionsFactory.BUY_VEHICLE_SLOT)


def buyBerths():
    ActionsFactory.doAction(ActionsFactory.BUY_BERTHS)


def createClan():
    g_eventBus.handleEvent(OpenLinkEvent(OpenLinkEvent.CLAN_CREATE))


def showMarathonPage():
    showMissionsMarathon()


def showShopPremium():
    showShop(shop_helpers.getBuyPremiumUrl())


def showShopEquipment():
    showShop(shop_helpers.getBuyEquipmentUrl())


def showShopOptionalDevice():
    showShop(shop_helpers.getBuyOptionalDevicesUrl())


def showShopPersonalReserves():
    showShop(shop_helpers.getBuyPersonalReservesUrl())


def showShopVehicles():
    showShop(shop_helpers.getBuyVehiclesUrl())


def showShopVehiclesRent():
    showShop(shop_helpers.getBuyVehiclesUrl())


def showShopVehiclesTradeIn():
    showShop(shop_helpers.getTradeInVehiclesUrl())


def configureShopForShells():
    AccountSettings.setFilter('shop_current', (-1, STORE_CONSTANTS.SHELL, True))
    shellsFilter = AccountSettings.getFilter('shop_shell')
    shellsFilter['fitsType'] = STORE_CONSTANTS.OTHER_VEHICLES_SHELL_FIT
    shellsFilter['itemTypes'] = [
     STORE_CONSTANTS.ARMOR_PIERCING_SHELL,
     STORE_CONSTANTS.ARMOR_PIERCING_CR_SHELL,
     STORE_CONSTANTS.HOLLOW_CHARGE_SHELL,
     STORE_CONSTANTS.HIGH_EXPLOSIVE_SHELL]
    AccountSettings.setFilter('shop_shell', shellsFilter)


def showAdventCalendarFromAction():
    calendarCtrl = dependency.instance(ICalendarController)
    calendarCtrl.showWindow(invokedFrom=CalendarInvokeOrigin.ACTION)