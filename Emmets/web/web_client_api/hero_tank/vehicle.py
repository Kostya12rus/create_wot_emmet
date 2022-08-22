# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/hero_tank/vehicle.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared import event_dispatcher
from helpers import dependency
from skeletons.gui.game_control import IHeroTankController
from web.web_client_api import w2c, W2CSchema

class HeroTankWebApiMixin(object):
    __heroControl = dependency.descriptor(IHeroTankController)

    @w2c(W2CSchema, 'get_id')
    def getName(self, _):
        return self.__heroControl.getCurrentTankCD()

    @w2c(W2CSchema, 'show_preview')
    def showPreview(self, _):
        tankCd = self.__heroControl.getCurrentTankCD()
        if tankCd:
            event_dispatcher.goToHeroTankOnScene(tankCd, previewAlias=VIEW_ALIAS.LOBBY_STORE)