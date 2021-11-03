# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/processors/messages/items_processor_messages.py
import logging
from gui.SystemMessages import SM_TYPE, CURRENCY_TO_SM_TYPE, CURRENCY_TO_SM_TYPE_DISMANTLING
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import formatPrice
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_ZERO
from gui.shared.gui_items.processors import makeSuccess, makeError
from gui.shared.money import ZERO_MONEY
from helpers import dependency
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

class _ItemProcessorMessage(object):
    _ITEMS_MSG_PREFIXES = {GUI_ITEM_TYPE.SHELL: 'shell', 
       GUI_ITEM_TYPE.EQUIPMENT: 'artefact', 
       GUI_ITEM_TYPE.OPTIONALDEVICE: 'artefact', 
       GUI_ITEM_TYPE.BATTLE_BOOSTER: 'battleBooster', 
       GUI_ITEM_TYPE.CREW_BOOKS: 'crewBooks'}
    _ITEMS_MSG_PREFIXES.update({typeID:'module' for typeID in GUI_ITEM_TYPE.VEHICLE_MODULES})
    __slots__ = ('_item', )

    def __init__(self, item):
        self._item = item

    def makeErrorMsg(self, reason):
        msgKey = R.strings.system_messages.dyn(self._formMessage()).dyn(reason)
        return makeError(backport.text((msgKey() if msgKey else ''), **self._getMsgCtx()), self._getErrorMsgType())

    def makeSuccessMsg(self):
        msgKey = R.strings.system_messages.dyn(self._formMessage()).success
        return makeSuccess(backport.text((msgKey() if msgKey else ''), **self._getMsgCtx()), self._getSuccessMsgType())

    def _formMessage(self):
        return ('{itemType}_{opType}').format(itemType=self._ITEMS_MSG_PREFIXES.get(self._item.itemTypeID, ''), opType=self._getOperation())

    def _getErrorMsgType(self):
        return SM_TYPE.Error

    def _getSuccessMsgType(self):
        return SM_TYPE.Information

    def _getMsgCtx(self):
        raise NotImplementedError

    def _getOperation(self):
        raise NotImplementedError


class ItemBuyProcessorMessage(_ItemProcessorMessage):

    def __init__(self, item, itemCount, responsePrice=None):
        self.__count = itemCount
        self.__responsePrice = responsePrice
        super(ItemBuyProcessorMessage, self).__init__(item)

    def _getSuccessMsgType(self):
        return CURRENCY_TO_SM_TYPE.get(self.__getPrice().getCurrency(), SM_TYPE.PurchaseForCredits)

    def _getMsgCtx(self):
        price = self.__getPrice().price if self.__responsePrice is None else self.__responsePrice
        return {'name': self._item.userName, 
           'kind': self._item.userType, 
           'count': backport.getIntegralFormat(int(self.__count)), 
           'money': formatPrice(price, ignoreZeros=True)}

    def _getOperation(self):
        return 'buy'

    def __getPrice(self):
        return self._item.getBuyPrice()


class ItemInstallProcessorMessage(_ItemProcessorMessage):

    def _getMsgCtx(self):
        return {'name': self._item.userName, 
           'kind': self._item.userType}

    def _getOperation(self):
        return 'apply'


class ItemDestroyProcessorMessage(_ItemProcessorMessage):

    def _getMsgCtx(self):
        return {'name': self._item.userName, 
           'kind': self._item.userType}

    def _getOperation(self):
        return 'destroy'


class ItemRemoveProcessorMessage(_ItemProcessorMessage):

    def _getMsgCtx(self):
        return {'name': self._item.userName, 
           'kind': self._item.userType}

    def _getOperation(self):
        return 'remove'


class OptDeviceRemoveProcessorMessage(ItemRemoveProcessorMessage):
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, item, removalPrice=ZERO_MONEY, useDemountKit=False):
        self.__removalPrice = removalPrice
        self.__useDemountKit = useDemountKit
        super(OptDeviceRemoveProcessorMessage, self).__init__(item)

    def makeSuccessMsg(self):
        defaultKey = R.strings.system_messages.dyn(self._formMessage()).success
        if self.__useDemountKit:
            msgKey = R.strings.system_messages.dyn(self._formMessage()).demount_kit_success
        else:
            msgKey = R.strings.system_messages.dyn(self._formMessage()).money_success
        return makeSuccess(backport.text((msgKey() if msgKey else defaultKey), **self._getMsgCtx()), self._getSuccessMsgType())

    def _getSuccessMsgType(self):
        if self.__useDemountKit:
            return SM_TYPE.DismantlingForDemountKit
        return CURRENCY_TO_SM_TYPE_DISMANTLING.get(self.__removalPrice.getCurrency(), SM_TYPE.DismantlingForGold)

    def _getMsgCtx(self):
        return {'name': self._item.userName, 
           'kind': self._item.userType, 
           'money': formatPrice(self.__removalPrice, ignoreZeros=True)}


class BaseLayoutProcessorMessage(object):
    __slots__ = ()

    def makeErrorMsg(self, reason):
        layoutKey = R.strings.system_messages.dyn(self._formMessage())
        msgKey = layoutKey.dyn(reason) if layoutKey and reason else None
        return makeError(backport.text((msgKey() if msgKey else R.strings.system_messages.dyn(self._formMessage()).error()), **self._getMsgCtx()), self._getErrorMsgType())

    def makeSuccessMsg(self):
        layoutKey = R.strings.system_messages.dyn(self._formMessage())
        msgKey = layoutKey.dyn('success') if layoutKey else None
        return makeSuccess(backport.text((msgKey() if msgKey else ''), **self._getMsgCtx()), self._getSuccessMsgType())

    def _formMessage(self):
        return ('{layoutType}_{opType}').format(layoutType=self._getLayoutPrefix(), opType=self._getOperation())

    def _getErrorMsgType(self):
        return SM_TYPE.Error

    def _getSuccessMsgType(self):
        return SM_TYPE.Information

    def _getLayoutPrefix(self):
        return ''

    def _getMsgCtx(self):
        return {}

    def _getOperation(self):
        return ''


class LayoutApplyProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = ('_vehicle', '__responsePrice')

    def __init__(self, vehicle, responsePrice=None):
        self._vehicle = vehicle
        self.__responsePrice = responsePrice

    def makeSuccessMsg(self):
        layoutKey = R.strings.system_messages.dyn(self._formMessage())
        msgKey = layoutKey.success_money_spent if layoutKey else None
        return makeSuccess(backport.text((msgKey() if msgKey else ''), **self._getMsgCtx()), self._getSuccessMsgType())

    def _getSuccessMsgType(self):
        return CURRENCY_TO_SM_TYPE.get(self.__getPrice().getCurrency(byWeight=False), SM_TYPE.Information)

    def _getLayoutPrefix(self):
        return 'layout'

    def _getMsgCtx(self):
        price = self.__getPrice().price if self.__responsePrice is None else self.__responsePrice
        return {'vehName': self._vehicle.userName, 
           'money': formatPrice(price, ignoreZeros=True)}

    def _getOperation(self):
        return 'apply'

    def __getPrice(self):
        return sum([ item.getBuyPrice() for item in self._vehicle.shells.layout.getItems() if not item.isInInventory and item not in self._vehicle.shells.installed
                   ], ITEM_PRICE_ZERO)


class OptDevicesApplyProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return 'optionalDevices'

    def _getOperation(self):
        return 'apply'


class OptDevicesDemountProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return 'optionalDevices'

    def _getOperation(self):
        return 'remove'


class BattleAbilitiesApplyProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return 'battleAbilities'

    def _getOperation(self):
        return 'apply'


class ShellsApplyProcessorMessage(LayoutApplyProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return 'shells'

    def _getOperation(self):
        return 'apply'


class ConsumablesApplyProcessorMessage(LayoutApplyProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return 'consumables'

    def _getOperation(self):
        return 'apply'


class BattleBoostersApplyProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return 'battleBoosters'

    def _getOperation(self):
        return 'apply'