# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/LobbyChannelWindow.py
from constants import PREBATTLE_TYPE
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE, TARGET_ID
from gui.Scaleform.managers.windows_stored_data import stored_window
from gui.Scaleform.locale.MESSENGER import MESSENGER
from gui.shared.formatters import text_styles, icons
from helpers import i18n
from messenger.ext.channel_num_gen import getClientID4Prebattle
from messenger.gui.Scaleform.data.MembersDataProvider import MembersDataProvider
from messenger.gui.Scaleform.meta.LobbyChannelWindowMeta import LobbyChannelWindowMeta
from messenger.gui.Scaleform.view.lobby import antispam_message
from messenger.m_constants import PROTO_TYPE

def _tryToSetTrusted(window, storedData):
    if window.getProtoType() == PROTO_TYPE.BW_CHAT2 and window.getClientID() == getClientID4Prebattle(PREBATTLE_TYPE.TRAINING):
        storedData.setTrusted(True)


@stored_window(DATA_TYPE.CHANNEL_WINDOW, TARGET_ID.CHANNEL_CAROUSEL, sideEffect=_tryToSetTrusted)
class LobbyChannelWindow(LobbyChannelWindowMeta):

    def onWarningClose(self):
        antispam_message.close()

    def _populate(self):
        super(LobbyChannelWindow, self)._populate()
        channel = self._controller.getChannel()
        if self._controller.hasUntrustedMembers() and antispam_message.isShown():
            self.as_showWarningS(('{} {}\n{}').format(icons.markerBlocked(), text_styles.error(i18n.makeString(MESSENGER.CHAT_PERSONALMESSAGE_WARNINGHEAD)), i18n.makeString(MESSENGER.CHAT_PERSONALMESSAGE_WARNINGBODY)))
        self.as_setIsPrivateS(channel.isPrivate())
        if channel.haveMembers():
            membersDP = MembersDataProvider()
            membersDP.setFlashObject(self.as_getMembersDPS())
            self._controller.setMembersDP(membersDP)
        else:
            self.as_hideMembersListS()

    def _dispose(self):
        if self._controller is not None:
            self._controller.removeMembersDP()
        super(LobbyChannelWindow, self)._dispose()
        return