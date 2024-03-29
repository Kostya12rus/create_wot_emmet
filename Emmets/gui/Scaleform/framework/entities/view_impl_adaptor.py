# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/view_impl_adaptor.py
import typing, BigWorld
from frameworks.wulf import WindowStatus, WindowSettings, Window
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.entities.DisposableEntity import DisposableEntity
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.framework.entities.view_interface import ViewInterface
from gui.Scaleform.framework.settings import UIFrameworkImpl
from soft_exception import SoftException

class ViewImplAdaptor(DisposableEntity, ViewInterface):
    __slots__ = ('__window', '__loadID', '__scope', '__key', '__layer')

    def __init__(self):
        super(ViewImplAdaptor, self).__init__()
        self.__window = None
        self.__loadID = None
        self.__scope = ScopeTemplates.DEFAULT_SCOPE
        self.__key = None
        self.__layer = None
        return

    def __repr__(self):
        return ('{}(key={})').format(self.__class__.__name__, self.__key)

    @property
    def view(self):
        return self.__window.content

    @property
    def uiImpl(self):
        return UIFrameworkImpl.GUI_IMPL

    @property
    def layer(self):
        return self.__layer

    @property
    def viewScope(self):
        return self.__scope

    @property
    def key(self):
        return self.__key

    @property
    def alias(self):
        return self.__key.alias

    @property
    def uniqueName(self):
        return self.__key.name

    @property
    def settings(self):
        return

    @property
    def soundManager(self):
        return self.view.soundManager

    def isViewModal(self):
        return False

    def getAlias(self):
        return self.view.layoutID

    def setAlias(self, alias):
        raise SoftException('This method is not implemented')

    def getSubContainersSettings(self):
        return ()

    def getUniqueName(self):
        return self.__key.name

    def setUniqueName(self, name):
        raise SoftException('This method is not implemented')

    def getCurrentScope(self):
        return self.__scope

    def setCurrentScope(self, scope):
        self.__scope = scope

    def isLoaded(self):
        if self.__window is None:
            return False
        else:
            return self.__window.windowStatus == WindowStatus.LOADED

    def setView(self, view, parent=None):
        self.__layer = view.layer
        self.__key = ViewKey(view.layoutID, view.uniqueID)
        settings = WindowSettings()
        settings.content = view
        settings.parent = parent
        settings.layer = self.__layer
        self.__window = Window(settings)
        self.__window.onStatusChanged += self.__onStatusChanged

    def loadView(self):
        if self.__loadID is not None:
            BigWorld.cancelCallback(self.__loadID)
            self.__loadID = None
        self.__loadID = BigWorld.callback(0.0, self.__startToLoad)
        return

    def destroy(self):
        if self.__loadID is not None:
            BigWorld.cancelCallback(self.__loadID)
            self.__loadID = None
        if self.__window is not None:
            self.__window.onStatusChanged -= self.__onStatusChanged
        super(ViewImplAdaptor, self).destroy()
        return

    def _destroy(self):
        if self.__window is not None:
            self.__window.destroy()
            self.__window = None
        return

    def __onStatusChanged(self, state):
        if state == WindowStatus.LOADED:
            self.create()
        elif state == WindowStatus.DESTROYED:
            if self.__window is not None:
                self.__window.onStatusChanged -= self.__onStatusChanged
                self.__window = None
            self.destroy()
        return

    def __startToLoad(self):
        self.__loadID = None
        if self.__window is None:
            raise SoftException('Window is not defined.')
        self.__window.load()
        return