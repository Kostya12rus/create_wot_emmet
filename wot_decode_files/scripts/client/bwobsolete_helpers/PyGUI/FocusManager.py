# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/FocusManager.py
_focusedComponent = None

def getFocusedComponent():
    global _focusedComponent
    return _focusedComponent


def setFocusedComponent(newFocus):
    global _focusedComponent
    if newFocus != _focusedComponent:
        if _focusedComponent is not None:
            _focusedComponent.focus = False
        _focusedComponent = newFocus
        if newFocus is not None:
            newFocus.focus = True
    return


def isFocusedComponent(component):
    if _focusedComponent is None or component is None:
        return _focusedComponent is component
    else:
        return _focusedComponent.__str__() == component.__str__()