# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/crew_intro_view.py
from base_crew_view import BaseCrewSubView
from frameworks.wulf import ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.crew_intro_view_model import CrewIntroViewModel
from gui.impl.pub.lobby_window import LobbyWindow
from account_helpers.settings_core.settings_constants import GuiSettingsBehavior
from gui.shared.account_settings_helper import AccountSettingsHelper

class CrewIntroView(BaseCrewSubView):
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