# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/login_modes/steam_mode.py
import WGC
from gui import DialogsInterface
from base_wgc_mode import BaseWgcMode
from helpers import dependency
from skeletons.gameplay import IGameplayLogic

class SteamMode(BaseWgcMode):
    __gameplay = dependency.descriptor(IGameplayLogic)

    def __init__(self, view):
        super(SteamMode, self).__init__(view, None)
        return

    def onPopulate(self):
        if self.__checkWgcAvailable():
            super(SteamMode, self).onPopulate()

    def updateForm(self):
        if self._loginManager.wgcAvailable:
            self._view.as_showSteamLoginFormS({'userName': WGC.getUserName()})
        else:
            self._view.as_showSteamLoginFormS({})

    def _onWgcError(self):
        self._loginManager.tryPrepareWGCLogin()
        self.__checkWgcAvailable()

    def __checkWgcAvailable(self):
        if not self._loginManager.wgcAvailable:
            DialogsInterface.showI18nInfoDialog('steamStartNeeded', self.__onDialogCallback)
            return False
        return True

    def __onDialogCallback(self, _):
        self.__gameplay.quitFromGame()