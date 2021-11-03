# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ChannelComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ChannelComponentMeta(BaseDAAPIComponent):

    def isJoined(self):
        self._printOverrideError('isJoined')

    def sendMessage(self, message):
        self._printOverrideError('sendMessage')

    def getHistory(self):
        self._printOverrideError('getHistory')

    def getMessageMaxLength(self):
        self._printOverrideError('getMessageMaxLength')

    def onLinkClick(self, linkCode):
        self._printOverrideError('onLinkClick')

    def as_notifyInfoChangedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_notifyInfoChanged()

    def as_setJoinedS(self, flag):
        if self._isDAAPIInited():
            return self.flashObject.as_setJoined(flag)

    def as_addMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_addMessage(message)

    def as_getLastUnsentMessageS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getLastUnsentMessage()

    def as_setLastUnsentMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setLastUnsentMessage(message)