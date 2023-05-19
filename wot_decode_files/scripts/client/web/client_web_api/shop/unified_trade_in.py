# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/shop/unified_trade_in.py
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.shared import events
from helpers import dependency
from skeletons.gui.game_control import ITradeInController
from web.client_web_api.api import C2WHandler, c2w

class UnifiedTradeInEventHandler(C2WHandler, EventSystemEntity):
    __tradeIn = dependency.descriptor(ITradeInController)

    def __init__(self, sender):
        super(UnifiedTradeInEventHandler, self).__init__(sender)
        self.tradeInHelper = None
        return

    def init(self):
        super(UnifiedTradeInEventHandler, self).init()
        self.addListener(events.VehicleBuyEvent.VEHICLE_SELECTED, self.__onTradeInDataChanged)
        g_clientUpdateManager.addCallback('tokens', self.__onTokensUpdate)

    def fini(self):
        self.removeListener(events.VehicleBuyEvent.VEHICLE_SELECTED, self.__onTradeInDataChanged)
        g_clientUpdateManager.removeObjectCallbacks(self, True)
        super(UnifiedTradeInEventHandler, self).fini()

    def __onTokensUpdate(self, diff):
        if self.__tradeIn.getConfig().allAccessTokenSet.intersection(diff.keys()):
            self.__onTradeInDataChanged()

    @c2w(name='unified_trade_in_update')
    def __onTradeInDataChanged(self, *args, **kwargs):
        return