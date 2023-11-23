# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/view_overrider.py
import typing, Event
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from typing import Callable, Any, Dict, Tuple, Optional, Union
    from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams, ViewLoadParams

class ViewOverrider(object):
    __slots__ = ('__delegates', 'onViewOverriden', '__lastOverrides')
    __gui = dependency.descriptor(IGuiLoader)

    def __init__(self):
        self.__delegates = {}
        self.__lastOverrides = {}
        self.onViewOverriden = Event.Event()

    def getOverrideData(self, loadParams, *args, **kwargs):
        alias = loadParams.viewKey.alias
        for delegate in self.__delegates.get(alias, ()):
            overrideData = delegate(loadParams, *args, **kwargs)
            if overrideData:
                self.__lastOverrides[alias] = overrideData.loadParams.viewKey.alias
                self.onViewOverriden(alias, overrideData)
                return overrideData

        return

    def addOverride(self, alias, delegate):
        self.__delegates.setdefault(alias, set()).add(delegate)

    def removeOverride(self, alias, delegate):
        self.__delegates.get(alias, set()).discard(delegate)

    def isViewOverriden(self, alias):
        contentResId = self.__lastOverrides.get(alias)
        return contentResId is not None and self.__gui.windowsManager.getViewByLayoutID(contentResId) is not None


class OverrideData(object):
    __slots__ = ('__loadParams', '__args', '__kwargs')

    def __init__(self, loadParams, *args, **kwargs):
        self.__loadParams = loadParams
        self.__args = args
        self.__kwargs = kwargs

    @property
    def loadParams(self):
        return self.__loadParams

    @property
    def args(self):
        return self.__args

    @property
    def kwargs(self):
        return self.__kwargs