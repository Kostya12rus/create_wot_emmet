# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/listener.py
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader, GuiGlobalSpaceID

class AppLoaderListener(object):
    appLoader = dependency.descriptor(IAppLoader)

    def __init__(self):
        super(AppLoaderListener, self).__init__()
        self.__loader = None
        return

    def start(self, loader):
        self.__loader = loader
        self.appLoader.onGUISpaceEntered += self.__onGUISpaceEntered
        self.appLoader.onGUISpaceLeft += self.__onGUISpaceLeft
        self.appLoader.onGUISpaceBeforeEnter += self.__onGUISpaceBeforeEnter

    def stop(self):
        self.appLoader.onGUISpaceEntered -= self.__onGUISpaceEntered
        self.appLoader.onGUISpaceLeft -= self.__onGUISpaceLeft
        self.appLoader.onGUISpaceBeforeEnter -= self.__onGUISpaceBeforeEnter

    def __onGUISpaceEntered(self, spaceID):
        if spaceID == GuiGlobalSpaceID.LOGIN:
            self.__loader.goToLogin()
        elif spaceID == GuiGlobalSpaceID.LOBBY:
            self.__loader.goToLobby()
        elif spaceID == GuiGlobalSpaceID.BATTLE_LOADING:
            self.__loader.goToBattleLoading()
        elif spaceID == GuiGlobalSpaceID.BATTLE:
            self.__loader.goToBattle()

    def __onGUISpaceLeft(self, spaceID):
        if spaceID == GuiGlobalSpaceID.LOBBY:
            self.__loader.leaveLobby()
        elif spaceID == GuiGlobalSpaceID.BATTLE:
            self.__loader.leaveBattle()

    def __onGUISpaceBeforeEnter(self, spaceID):
        if spaceID == GuiGlobalSpaceID.LOBBY:
            self.__loader.beforeEnterLobby()
        elif spaceID == GuiGlobalSpaceID.BATTLE:
            self.__loader.beforeEnterBattle()