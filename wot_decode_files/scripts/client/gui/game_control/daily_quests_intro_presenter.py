# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/daily_quests_intro_presenter.py
from account_helpers.AccountSettings import Winback
from frameworks.wulf import ViewStatus
from gui.battle_pass.battle_pass_helpers import isBattlePassDailyQuestsIntroShown, showBattlePassDailyQuestsIntro, setBattlePassDailyQuestsIntroShown
from gui.impl.gen import R
from gui.shared import event_dispatcher
from gui.winback.winback_helpers import getWinbackSetting, setWinbackSetting
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IBattlePassController, IWinbackController, IDailyQuestIntroPresenter
from skeletons.gui.impl import IGuiLoader

class DailyQuestsIntroPresenter(IDailyQuestIntroPresenter):
    __slots__ = ()
    __settingsCore = dependency.descriptor(ISettingsCore)
    __guiLoader = dependency.descriptor(IGuiLoader)
    __winbackController = dependency.descriptor(IWinbackController)
    __battlePassController = dependency.descriptor(IBattlePassController)

    @property
    def parentViewLayoutID(self):
        return R.views.lobby.missions.Daily()

    def onLobbyStarted(self, *_):
        self.__addListeners()
        self.__update()

    def onAccountBecomeNonPlayer(self):
        self.__clearListeners()

    def fini(self):
        self.__clearListeners()

    def __addListeners(self):
        if self.__guiLoader.windowsManager is not None:
            self.__guiLoader.windowsManager.onViewStatusChanged += self.__onViewStatusChanged
        return

    def __clearListeners(self):
        if self.__guiLoader.windowsManager is not None:
            self.__guiLoader.windowsManager.onViewStatusChanged -= self.__onViewStatusChanged
        return

    def __onViewStatusChanged(self, uniqueID, newStatus):
        if newStatus == ViewStatus.LOADED:
            if self.__guiLoader.windowsManager.getView(uniqueID).layoutID == self.parentViewLayoutID:
                self.__update()

    def __update(self, *_):
        if self.__isDailyQuestView():
            if self.__winbackController.isProgressionAvailable() and not self.__isWinbackIntroShown():
                self.__showWinbackIntroScreen()
                if self.__battlePassController.isActive():
                    setBattlePassDailyQuestsIntroShown()
            elif self.__battlePassController.isActive() and not isBattlePassDailyQuestsIntroShown():
                showBattlePassDailyQuestsIntro()

    def __isDailyQuestView(self):
        return self.__guiLoader.windowsManager.getViewByLayoutID(self.parentViewLayoutID) is not None

    def __isWinbackIntroShown(self):
        return getWinbackSetting(Winback.INTRO_SHOWN)

    def __showWinbackIntroScreen(self):
        event_dispatcher.showWinbackIntroView()
        setWinbackSetting(Winback.INTRO_SHOWN, True)