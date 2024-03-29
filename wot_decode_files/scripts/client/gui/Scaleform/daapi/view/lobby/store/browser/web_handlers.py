# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/store/browser/web_handlers.py
from gui.shared.event_dispatcher import showShop
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from web.web_client_api import webApiCollection
from web.web_client_api.clans import ClansWebApi
from web.web_client_api.platform import PlatformWebApi
from web.web_client_api.quests import QuestsWebApi
from web.web_client_api.loot_boxes import LootBoxWebApi
from web.web_client_api.ranked_battles import RankedBattlesWebApi
from web.web_client_api.request import RequestWebApi
from web.web_client_api.sound import SoundWebApi, SoundStateWebApi, HangarSoundWebApi
from web.web_client_api.shop import ShopWebApi
from web.web_client_api.hero_tank import HeroTankWebApi
from web.web_client_api.battle_pass import BattlePassWebApi
from web.web_client_api.ui import NotificationWebApi, OpenWindowWebApi, OpenTabWebApi, CloseWindowWebApi, UtilWebApi
from web.web_client_api.frontline import FrontLineWebApi
from web.web_client_api.blueprints_convert_sale import BlueprintsConvertSaleWebApi
from web.web_client_api.uilogging import UILoggingWebApi

class _OpenTabWebApi(OpenTabWebApi):

    def _getVehiclePreviewReturnAlias(self, cmd):
        return VIEW_ALIAS.LOBBY_STORE

    def _getVehiclePreviewReturnCallback(self, cmd):
        return self.__getReturnCallback(cmd.back_url)

    def _getVehicleStylePreviewCallback(self, cmd):
        return self.__getReturnCallback(cmd.back_url)

    def __getReturnCallback(self, backUrl):
        if backUrl is not None:
            return (lambda : showShop(backUrl))
        else:
            return


def createShopWebHandlers():
    return webApiCollection(CloseWindowWebApi, OpenWindowWebApi, NotificationWebApi, _OpenTabWebApi, RequestWebApi, ShopWebApi, SoundWebApi, SoundStateWebApi, HangarSoundWebApi, UtilWebApi, FrontLineWebApi, HeroTankWebApi, BattlePassWebApi, ClansWebApi, RankedBattlesWebApi, BlueprintsConvertSaleWebApi, PlatformWebApi, QuestsWebApi, LootBoxWebApi, UILoggingWebApi)