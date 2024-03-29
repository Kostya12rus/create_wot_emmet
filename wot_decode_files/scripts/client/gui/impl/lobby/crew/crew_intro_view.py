# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/crew_intro_view.py
from frameworks.wulf import ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.crew_intro_view_model import CrewIntroViewModel
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from account_helpers.settings_core.settings_constants import GuiSettingsBehavior
from gui.shared.account_settings_helper import AccountSettingsHelper

class CrewIntroView(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.crew.CrewIntroView())
        settings.model = CrewIntroViewModel()
        super(CrewIntroView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CrewIntroView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__close),)

    def __close(self):
        AccountSettingsHelper.welcomeScreenShown(GuiSettingsBehavior.CREW_22_WELCOME_SHOWN)
        self.destroyWindow()


class CrewIntroWindow(LobbyWindow):
    __slots__ = ()

    def __init__(self):
        super(CrewIntroWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=CrewIntroView())