# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/wot_anniversary/__init__.py
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.wot_anniversary.wot_anniversary_helpers import WOT_ANNIVERSARY_PREFIX
from web.client_web_api.api import C2WHandler, c2w

class WotAnniversaryEventHandler(C2WHandler):

    def init(self):
        super(WotAnniversaryEventHandler, self).init()
        g_clientUpdateManager.addCallback('tokens', self.__onTokensUpdate)

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self, True)
        super(WotAnniversaryEventHandler, self).fini()

    def __onTokensUpdate(self, diff):
        for tID in diff.keys():
            if tID.startswith(WOT_ANNIVERSARY_PREFIX):
                self.__sendTokens()
                return

    @c2w(name='wot_anniversary_tokens_changed')
    def __sendTokens(self):
        return