# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ConnectToSecureChannelWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConnectToSecureChannelWindowMeta(AbstractWindowView):

    def sendPassword(self, value):
        self._printOverrideError('sendPassword')

    def cancelPassword(self):
        self._printOverrideError('cancelPassword')

    def as_infoMessageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_infoMessage(value)