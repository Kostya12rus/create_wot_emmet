# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/shop/telecom_rentals.py
from gui.ClientUpdateManager import g_clientUpdateManager
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from telecom_rentals_common import PARTNERSHIP_TOKEN_NAME, TELECOM_RENTALS_CONFIG, PARTNERSHIP_BLOCKED_TOKEN_NAME
from web.client_web_api.api import C2WHandler, c2w

class TelecomTokenEventHandler(C2WHandler):
    _lobbyContext = dependency.descriptor(ILobbyContext)

    def init(self):
        super(TelecomTokenEventHandler, self).init()
        g_clientUpdateManager.addCallback('tokens', self.__onTokensUpdate)
        self._lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self, True)
        self._lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        super(TelecomTokenEventHandler, self).fini()

    def __onServerSettingChanged(self, diff):
        if TELECOM_RENTALS_CONFIG in diff:
            self.__sendNotify()

    def __onTokensUpdate(self, diff):
        if {PARTNERSHIP_TOKEN_NAME, PARTNERSHIP_BLOCKED_TOKEN_NAME}.intersection(diff.keys()):
            self.__sendNotify()

    @c2w(name='telecom_token_update')
    def __sendNotify(self):
        return