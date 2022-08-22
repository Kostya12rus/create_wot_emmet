# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/badges.py
from web.web_client_api import w2c, W2CSchema
from gui.shared import event_dispatcher as shared_events

class BadgesWebApiMixin(object):

    @w2c(W2CSchema, 'badges')
    def openBadges(self, cmd):
        shared_events.showBadges()