# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/debut_boxes/debut_boxes_browser_view.py
from gui.impl.lobby.common.browser_view import BrowserView
from helpers import dependency
from skeletons.gui.game_control import IDebutBoxesController

class DebutBoxesBrowserView(BrowserView):
    __debutBoxesController = dependency.descriptor(IDebutBoxesController)

    def _onLoading(self, *args, **kwargs):
        super(DebutBoxesBrowserView, self)._onLoading(*args, **kwargs)
        self.__debutBoxesController.onStateChanged += self.__onStateChanged

    def _finalize(self):
        self.__debutBoxesController.onStateChanged -= self.__onStateChanged
        super(DebutBoxesBrowserView, self)._finalize()

    def __onStateChanged(self):
        if not self.__debutBoxesController.isEnabled():
            self.onCloseView()