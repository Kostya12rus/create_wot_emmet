# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/impl.py
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from Event import Event
    from frameworks.wulf import ViewModel
    from frameworks.wulf.tutorial import Tutorial
    from frameworks.wulf.ui_logger import UILogger

class IGuiLoader(object):
    __slots__ = ()

    @property
    def resourceManager(self):
        raise NotImplementedError

    @property
    def windowsManager(self):
        raise NotImplementedError

    @property
    def systemLocale(self):
        raise NotImplementedError

    @property
    def tutorial(self):
        raise NotImplementedError

    @property
    def uiLogger(self):
        raise NotImplementedError

    def init(self, tutorialModel, uiLoggerModel):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError


class INotificationWindowController(IGameController):
    __slots__ = ('onPostponedQueueUpdated', )
    if typing.TYPE_CHECKING:
        onPostponedQueueUpdated = None

    def append(self, window):
        raise NotImplementedError

    def hasWindow(self, window):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def postponeActive(self):
        raise NotImplementedError

    def releasePostponed(self):
        raise NotImplementedError

    def lock(self, key):
        raise NotImplementedError

    def unlock(self, key):
        raise NotImplementedError

    def hasLock(self, key):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    @property
    def postponedCount(self):
        raise NotImplementedError


class IFullscreenManager(object):
    __slots__ = ()

    def setEnabled(self, value):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError


class IWindowLoaderController(IGameController):
    __slots__ = ()


class IOverlaysManager(object):
    __slots__ = ()

    def isSuspended(self, window):
        raise NotImplementedError

    def suspend(self, condition=None):
        raise NotImplementedError

    def release(self):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError