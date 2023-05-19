# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/GameInputManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class GameInputManagerMeta(BaseDAAPIComponent):

    def handleGlobalKeyEvent(self, keyCode, eventType):
        self._printOverrideError('handleGlobalKeyEvent')

    def as_addKeyHandlerS(self, keyCode, eventType, ignoreText, cancelEventType=None, priority=0):
        if self._isDAAPIInited():
            return self.flashObject.as_addKeyHandler(keyCode, eventType, ignoreText, cancelEventType, priority)

    def as_clearKeyHandlerS(self, keyCode, eventType):
        if self._isDAAPIInited():
            return self.flashObject.as_clearKeyHandler(keyCode, eventType)