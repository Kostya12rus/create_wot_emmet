# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/settings.py
import helpers
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from helpers import dependency
from skeletons.gui.game_control import IUISpamController
from web.web_client_api import W2CSchema, w2c

class SettingsWebApiMixin(object):
    _uiSpamController = dependency.descriptor(IUISpamController)
    _MODE_HIDE_COUNTERS = 'hide_counters'

    @w2c(W2CSchema, 'settings')
    def getSettings(self, _):
        return {'client_version': helpers.getClientVersion(), 
           'ui_spam_mode': self._MODE_HIDE_COUNTERS if self._uiSpamController.shouldBeHidden(VIEW_ALIAS.LOBBY_STORE) else ''}