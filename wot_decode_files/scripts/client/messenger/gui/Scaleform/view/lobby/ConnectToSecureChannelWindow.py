# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/ConnectToSecureChannelWindow.py
from gui.Scaleform.locale.MESSENGER import MESSENGER
from helpers import i18n
from messenger.gui.Scaleform.meta.ConnectToSecureChannelWindowMeta import ConnectToSecureChannelWindowMeta
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.events import g_messengerEvents

class ConnectToSecureChannelWindow(ConnectToSecureChannelWindowMeta):

    def __init__(self, ctx=None):
        super(ConnectToSecureChannelWindow, self).__init__()
        self._channel = ctx.get('channel')

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    def onWindowClose(self):
        self.destroy()

    def sendPassword(self, value):
        validator = self.proto.messages.getUserRoomValidator()
        password, error = validator.validateUserRoomPwd(value)
        if error is not None:
            g_messengerEvents.onErrorReceived(error)
        else:
            self.proto.messages.joinToUserRoom(self._channel.getID(), self._channel.getFullName(), password=password)
            self.destroy()
        return

    def cancelPassword(self):
        self.destroy()

    def _populate(self):
        super(ConnectToSecureChannelWindow, self)._populate()
        self.as_infoMessageS(i18n.makeString(MESSENGER.DIALOGS_CONNECTINGTOSECURECHANNEL_LABELS_INFO, self._channel.getFullName()))

    def _dispose(self):
        self._channel = None
        super(ConnectToSecureChannelWindow, self)._dispose()
        return