# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/ClientSelectableWotAnniversaryObject.py
from ClientSelectableObject import ClientSelectableObject
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from account_helpers.settings_core.settings_constants import WotAnniversaryStorageKeys
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.wot_anniversary.wot_anniversary_helpers import showMainView, showWotAnniversaryIntroWindow
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IWotAnniversaryController

class ClientSelectableWotAnniversaryObject(ClientSelectableObject):
    __wotAnniversaryCtrl = dependency.descriptor(IWotAnniversaryController)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def onEnterWorld(self, prereqs):
        super(ClientSelectableWotAnniversaryObject, self).onEnterWorld(prereqs)
        self.__wotAnniversaryCtrl.onSettingsChanged += self.__onSettingsChanged
        self.__onSettingsChanged()

    def onLeaveWorld(self):
        self.__wotAnniversaryCtrl.onSettingsChanged -= self.__onSettingsChanged
        super(ClientSelectableWotAnniversaryObject, self).onLeaveWorld()

    def onMouseClick(self):
        super(ClientSelectableWotAnniversaryObject, self).onMouseClick()
        g_eventBus.handleEvent(events.WotAnniversaryEvent(events.WotAnniversaryEvent.ON_WIDGET_STATE_UPDATED), EVENT_BUS_SCOPE.LOBBY)
        if not self.__settingsCore.serverSettings.getSection(SETTINGS_SECTIONS.WOT_ANNIVERSARY_STORAGE).get(WotAnniversaryStorageKeys.WOT_ANNIVERSARY_INTRO_SHOWED):
            showWotAnniversaryIntroWindow(closeCallback=showMainView)
            return
        showMainView()

    def __onSettingsChanged(self, *_):
        if self.__wotAnniversaryCtrl.isAvailable():
            self.setEnable(True)
        else:
            self.setEnable(False)