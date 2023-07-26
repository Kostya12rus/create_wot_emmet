# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_presets/hangar_gui_helpers.py
import operator
from functools import wraps
from helpers import dependency
from skeletons.gui.game_control import IHangarGuiController

def ifComponentAvailable(componentType=None):

    def decorator(method):

        @wraps(method)
        def wrapper(hangar, *args, **kwargs):
            hangarGuiCtrl = dependency.instance(IHangarGuiController)
            if hangarGuiCtrl.isComponentAvailable(componentType):
                return method(hangar, *args, **kwargs)

        return wrapper

    return decorator


def ifComponentInPreset(componentType=None):

    def decorator(method):

        @wraps(method)
        def wrapper(presetGetter, *args, **kwargs):
            preset = presetGetter.getPreset()
            if preset is not None and componentType in preset.visibleComponents:
                return method(presetGetter, preset, *args, **kwargs)
            else:
                return

        return wrapper

    return decorator


def hasCurrentPreset(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(hangarGuiCtrl, *args, **kwargs):
            currentPreset = hangarGuiCtrl.getCurrentPreset()
            if currentPreset is not None:
                return method(hangarGuiCtrl, currentPreset, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(hangarGuiCtrl)
                return defReturn

        return wrapper

    return decorator