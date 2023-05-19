# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/Listeners.py
import weakref
_languageChangeListeners = []
_deviceListeners = []

def registerInputLangChangeListener(listener):
    global _languageChangeListeners
    _languageChangeListeners.append(weakref.ref(listener))


def registerDeviceListener(listener):
    _deviceListeners.append(weakref.ref(listener))


def handleInputLangChangeEvent():
    import GUI
    for listener in [ x() for x in _languageChangeListeners if x() is not None ]:
        if hasattr(listener, 'handleInputLangChangeEvent'):
            listener.handleInputLangChangeEvent()

    return True


def onRecreateDevice():
    for listener in [ x() for x in _deviceListeners if x() is not None ]:
        if hasattr(listener, 'onRecreateDevice'):
            listener.onRecreateDevice()

    return