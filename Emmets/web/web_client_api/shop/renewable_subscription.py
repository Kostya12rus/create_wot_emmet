# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/shop/renewable_subscription.py
import logging, BigWorld
from account_helpers.renewable_subscription import RenewableSubscription
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.event_dispatcher import showWotPlusInfoPage
from gui.shared.gui_items.Vehicle import getUserName
from items.vehicles import getVehicleType
from web.web_client_api import W2CSchema, w2c, Field
_logger = logging.getLogger(__name__)

class _RenewableSubRentVehicleInfoSchema(W2CSchema):
    vehCD = Field(required=True, type=int)


class RenewableSubWebApiMixin(object):

    @w2c(W2CSchema, 'get_subscription_info')
    def getSubscriptionInfo(self, cmd):
        helper = BigWorld.player().renewableSubscription
        return {'period_start': helper.getStartTime(), 
           'period_end': helper.getExpiryTime()}

    @w2c(W2CSchema, 'subscription_info_window')
    def handleSubscriptionInfoWindow(self, cmd):
        showWotPlusInfoPage()

    @w2c(_RenewableSubRentVehicleInfoSchema, 'subscription_rent_delayed')
    def subscriptionRentDelayed(self, cmd):
        if cmd.vehCD:
            BigWorld.player().renewableSubscription.setRentPending(cmd.vehCD)
            vehName = getUserName(getVehicleType(cmd.vehCD))
            SystemMessages.pushMessage('', messageData={'header': backport.text(R.strings.messenger.serviceChannelMessages.wotPlus.tankRental.isPending.title()), 
               'text': backport.text(R.strings.messenger.serviceChannelMessages.wotPlus.tankRental.isPending.text(), vehicle=vehName)}, type=SystemMessages.SM_TYPE.MessageHeader)