# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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