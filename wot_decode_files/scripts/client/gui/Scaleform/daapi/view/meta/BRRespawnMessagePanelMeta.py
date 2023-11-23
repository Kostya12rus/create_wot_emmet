# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BRRespawnMessagePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BRRespawnMessagePanelMeta(BaseDAAPIComponent):

    def as_addMessageS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addMessage(data)

    def as_hideMessageS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideMessage()

    def as_setMessageTimeS(self, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessageTime(seconds)