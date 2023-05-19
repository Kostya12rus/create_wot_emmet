# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/shop/vehicle_sell_confirmation_popover.py
import logging
from gui.Scaleform.daapi.view.meta.VehicleSellConfirmationPopoverMeta import VehicleSellConfirmationPopoverMeta
from gui.Scaleform.locale.STORE import STORE
from gui.impl import backport
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import ShopEvent
from gui.shared.formatters import text_styles
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

class VehicleSellConfirmationPopover(VehicleSellConfirmationPopoverMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx=None):
        super(VehicleSellConfirmationPopover, self).__init__(ctx)
        data = ctx.get('data')
        self.__confirmGoldPrice = int(data.confirmGoldPrice)
        self.__tradeOffVehicleIntCD = int(data.tradeOffVehicleIntCD)

    def confirmTradeIn(self):
        self.fireEvent(ShopEvent(ShopEvent.CONFIRM_TRADE_IN), EVENT_BUS_SCOPE.LOBBY)
        self.destroy()

    def _populate(self):
        super(VehicleSellConfirmationPopover, self)._populate()
        self.as_setInitDataS(self.__getInitialVO())

    def __getInitialVO(self):
        tradeOffVehicle = self.itemsCache.items.getItemByCD(self.__tradeOffVehicleIntCD)
        if tradeOffVehicle:
            dataVO = {'titleLabel': text_styles.main(_ms(STORE.SELLCONFIRMATIONPOPOVER_TITLELABEL, vehName=tradeOffVehicle.shortUserName)), 
               'priceLabel': text_styles.main(_ms(STORE.SELLCONFIRMATIONPOPOVER_PRICELABEL, price=text_styles.highlightText(backport.getIntegralFormat(self.__confirmGoldPrice)))), 
               'priceValue': self.__confirmGoldPrice}
            return dataVO
        else:
            _logger.error('Invalid trade off vehicle CD.')
            return