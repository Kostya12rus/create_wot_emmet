# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/login_modes/base_wgc_mode.py
import WGC
from account_helpers.settings_core.settings_constants import GAME
from base_mode import BaseMode
_g_firstEntry = True

class BaseWgcMode(BaseMode):

    @property
    def login(self):
        return WGC.getUserName()

    @property
    def showRememberServerWarning(self):
        return not self._loginManager.settingsCore.getSetting(GAME.LOGIN_SERVER_SELECTION) and self._loginManager.getPreference('server_select_was_set')

    def onPopulate(self):
        global _g_firstEntry
        if self._loginManager.wgcAvailable:
            self._loginManager.addOnWgcErrorListener(self._onWgcError)
        autoLogin = _g_firstEntry and not self._loginManager.settingsCore.getSetting(GAME.LOGIN_SERVER_SELECTION) and not self._loginManager.getPreference('server_select_was_set')
        if autoLogin:
            self._loginManager.tryWgcLogin()
        _g_firstEntry = False

    def doLogin(self, userName, password, serverName, isSocialToken2Login):
        self._loginManager.tryWgcLogin(serverName)

    def skipRejectionError(self, loginStatus):
        return self._loginManager.checkWgcCouldRetry(loginStatus)

    def updateForm(self):
        pass

    def destroy(self):
        if self._loginManager.wgcAvailable:
            self._loginManager.removeOnWgcErrorListener(self._onWgcError)
        super(BaseWgcMode, self).destroy()

    def _onWgcError(self):
        pass