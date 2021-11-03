# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/halloween/interrogation_info_page_view.py
from frameworks.wulf import ViewSettings, WindowLayer, WindowFlags
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.halloween.interrogation_info_page_view_model import InterrogationInfoPageViewModel
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.shared.view_helpers.blur_manager import CachedBlur
from helpers import dependency
from skeletons.gui.game_event_controller import IGameEventController
from skeletons.gui.server_events import IEventsCache

class InterrogationInfoPageView(ViewImpl):
    _gameEventController = dependency.descriptor(IGameEventController)
    _eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self):
        settings = ViewSettings(R.views.lobby.halloween.InterrogationInfoPageView())
        settings.model = InterrogationInfoPageViewModel()
        super(InterrogationInfoPageView, self).__init__(settings)
        self.__blur = None
        return

    @property
    def viewModel(self):
        return super(InterrogationInfoPageView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(InterrogationInfoPageView, self)._onLoading(*args, **kwargs)
        self.__blur = CachedBlur(enabled=True, ownLayer=WindowLayer.WINDOW)
        self._addListeners()

    def _finalize(self):
        self._removeListeners()
        if self.__blur:
            self.__blur.fini()
            self.__blur = None
        super(InterrogationInfoPageView, self)._finalize()
        return

    def _addListeners(self):
        self._gameEventController.onIngameEventsUpdated += self.__updateEvent
        self.viewModel.onAccept += self._onAccept
        self.viewModel.onClose += self._onClose

    def _removeListeners(self):
        self._gameEventController.onIngameEventsUpdated -= self.__updateEvent
        self.viewModel.onAccept -= self._onAccept
        self.viewModel.onClose -= self._onClose

    def _onAccept(self):
        self.destroyWindow()

    def _onClose(self):
        self.destroyWindow()

    def __updateEvent(self):
        if not self._eventsCache.isEventEnabled():
            self.destroyWindow()


class InterrogationInfoPageWindow(LobbyWindow):

    def __init__(self):
        super(InterrogationInfoPageWindow, self).__init__(content=InterrogationInfoPageView(), wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN)