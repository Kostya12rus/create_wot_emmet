# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/crew_intro_view.py
from frameworks.wulf import ViewSettings, WindowFlags
from gui import GUI_SETTINGS
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.crew_intro_view_model import CrewIntroViewModel
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from shared_utils import first

class CrewIntroView(ViewImpl):
    __slots__ = ('__screenName', '__onCloseCallback')

    def __init__(self, screenName, onCloseCallback=None):
        self.__screenName = screenName
        self.__onCloseCallback = onCloseCallback
        settings = ViewSettings(R.views.lobby.crew.CrewIntroView())
        settings.model = CrewIntroViewModel()
        super(CrewIntroView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CrewIntroView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CrewIntroView, self)._onLoading(*args, **kwargs)
        self.__updateViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__close),)

    def __updateViewModel(self):
        slideData = GUI_SETTINGS.crew.get('welcomeScreens', {}).get(self.__screenName, [])
        with self.viewModel.transaction() as (tx):
            tx.setScreenName(self.__screenName)
            slides = tx.getSlides()
            slides.clear()
            for value in slideData:
                slides.addNumber(value)

        slides.invalidate()

    def __close(self, *args):
        self.destroyWindow()
        if callable(self.__onCloseCallback):
            self.__onCloseCallback(first(args))


class CrewIntroWindow(LobbyWindow):
    __slots__ = ()

    def __init__(self, screenName, onCloseCallback=None):
        super(CrewIntroWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=CrewIntroView(screenName, onCloseCallback))