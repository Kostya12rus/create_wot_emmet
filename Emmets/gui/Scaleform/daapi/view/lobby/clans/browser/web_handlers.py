# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/browser/web_handlers.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared.event_dispatcher import showClanQuestWindow
from web.web_client_api import webApiCollection
from web.web_client_api.request import RequestWebApi
from web.web_client_api.rewards import RewardsWebApi
from web.web_client_api.shop import ShopWebApi
from web.web_client_api.social import SocialWebApi
from web.web_client_api.sound import SoundWebApi, SoundStateWebApi
from web.web_client_api.clans import ClansWebApi
from web.web_client_api.strongholds import StrongholdsWebApi
from web.web_client_api.ui import OpenWindowWebApi, OpenTabWebApi, UtilWebApi, ContextMenuWebApi, CloseWindowWebApi

class _OpenTabWebApi(OpenTabWebApi):

    def _getVehiclePreviewReturnAlias(self, cmd):
        return VIEW_ALIAS.CLAN_NOTIFICATION_WINDOW

    def _getVehiclePreviewReturnCallback(self, cmd):
        return self.__getReturnCallback(cmd.back_url)

    def __getReturnCallback(self, backUrl):
        if backUrl is not None:
            return (lambda : showClanQuestWindow(backUrl))
        else:
            return


def createNotificationWebHandlers():
    return webApiCollection(SoundWebApi, RequestWebApi, ContextMenuWebApi, OpenWindowWebApi, UtilWebApi, RewardsWebApi, SocialWebApi, ShopWebApi, CloseWindowWebApi, _OpenTabWebApi, ClansWebApi, SoundStateWebApi, StrongholdsWebApi)