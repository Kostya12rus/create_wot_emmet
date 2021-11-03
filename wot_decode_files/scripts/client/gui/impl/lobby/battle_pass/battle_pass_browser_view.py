# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/battle_pass_browser_view.py
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.server_events.events_dispatcher import showMissionsBattlePassCommonProgression
from gui.shared.event_dispatcher import showHangar
from gui.sounds.filters import switchHangarOverlaySoundFilter
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController
from web.web_client_api import webApiCollection, ui as ui_web_api, sound as sound_web_api
from web.web_client_api.battle_pass import BattlePassWebApi
from web.web_client_api.sound import SoundStateWebApi

class BattlePassBrowserView(WebView):
    __battlePassController = dependency.descriptor(IBattlePassController)

    def webHandlers(self):
        return webApiCollection(BattlePassWebApi, ui_web_api.OpenWindowWebApi, ui_web_api.CloseWindowWebApi, ui_web_api.OpenTabWebApi, ui_web_api.NotificationWebApi, ui_web_api.ContextMenuWebApi, ui_web_api.UtilWebApi, sound_web_api.SoundWebApi, sound_web_api.HangarSoundWebApi, SoundStateWebApi)

    def onCloseBtnClick(self):
        showMissionsBattlePassCommonProgression()
        self.destroy()

    def _populate(self):
        super(BattlePassBrowserView, self)._populate()
        self.__battlePassController.onBattlePassSettingsChange += self.__onSettingsChange
        switchHangarOverlaySoundFilter(on=True)

    def _dispose(self):
        super(BattlePassBrowserView, self)._dispose()
        self.__battlePassController.onBattlePassSettingsChange -= self.__onSettingsChange
        switchHangarOverlaySoundFilter(on=False)

    def __onSettingsChange(self, *_):
        if not self.__battlePassController.isVisible() or self.__battlePassController.isPaused():
            showHangar()