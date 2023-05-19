# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/premium.py
from web.web_client_api import w2c, W2CSchema
from gui.shared import event_dispatcher as shared_events

class PremiumViewsWebApiMixin(object):

    @w2c(W2CSchema, 'premium_dashboard')
    def openPremiumDashboardWindow(self, _):
        shared_events.showDashboardView()

    @w2c(W2CSchema, 'maps_blacklist')
    def openMapsBlacklistView(self, _):
        shared_events.showMapsBlacklistView()