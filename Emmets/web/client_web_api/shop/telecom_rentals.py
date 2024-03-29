# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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