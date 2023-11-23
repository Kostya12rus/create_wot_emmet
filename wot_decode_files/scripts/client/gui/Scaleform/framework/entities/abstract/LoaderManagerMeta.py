# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/LoaderManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class LoaderManagerMeta(BaseDAAPIComponent):

    def viewLoaded(self, alias, viewName, view):
        self._printOverrideError('viewLoaded')

    def viewLoadError(self, alias, viewName, text):
        self._printOverrideError('viewLoadError')

    def viewInitializationError(self, alias, viewName):
        self._printOverrideError('viewInitializationError')

    def viewLoadCanceled(self, alias, viewName):
        self._printOverrideError('viewLoadCanceled')

    def as_loadViewS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(data)

    def as_cancelLoadViewS(self, viewName):
        if self._isDAAPIInited():
            return self.flashObject.as_cancelLoadView(viewName)