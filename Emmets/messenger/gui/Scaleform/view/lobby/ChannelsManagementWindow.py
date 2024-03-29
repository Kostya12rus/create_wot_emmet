# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/ChannelsManagementWindow.py
from constants import IS_CHINA
from debug_utils import LOG_ERROR
from gui.Scaleform.locale.MESSENGER import MESSENGER
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE, TARGET_ID
from gui.Scaleform.managers.windows_stored_data import stored_window
from helpers import i18n
from messenger.gui.Scaleform.data.search_data_providers import SearchChannelsDataProvider
from messenger.gui.Scaleform.meta.ChannelsManagementWindowMeta import ChannelsManagementWindowMeta
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.events import g_messengerEvents
from messenger.proto.interfaces import ISearchHandler

@stored_window(DATA_TYPE.UNIQUE_WINDOW, TARGET_ID.CHAT_MANAGEMENT)
class ChannelsManagementWindow(ChannelsManagementWindowMeta, ISearchHandler):

    def __init__(self, _=None):
        super(ChannelsManagementWindow, self).__init__()
        self._searchDP = SearchChannelsDataProvider(self.proto.messages.getSearchUserRoomsProcessor())

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    def onWindowClose(self):
        self.destroy()

    def getSearchLimitLabel(self):
        return i18n.makeString(MESSENGER.DIALOGS_SEARCHCHANNEL_LABELS_RESULT, self._searchDP.processor.getSearchResultLimit())

    def searchToken(self, token):
        self.as_freezSearchButtonS(True)
        self._searchDP.find(token.strip())

    def joinToChannel(self, index):
        item = self._searchDP.requestItemAtHandler(int(index))
        if item is not None:
            self.proto.messages.joinToUserRoom(item['id'], item['name'])
        else:
            LOG_ERROR('Channel data not found', int(index))
        return

    def createChannel(self, name, usePassword, password, retype):
        validator = self.proto.messages.getUserRoomValidator()
        if not IS_CHINA:
            name, error = validator.validateUserRoomName(name)
            if error is not None:
                g_messengerEvents.onErrorReceived(error)
                return
        else:
            name, error = ('', None)
        if usePassword:
            _, error = validator.validateUserRoomPwdPair(password, retype)
            if error is not None:
                g_messengerEvents.onErrorReceived(error)
                return
        result = self.proto.messages.createUserRoom(name, password)
        if result:
            self.destroy()
        return

    def onSearchComplete(self, _):
        self.as_freezSearchButtonS(False)

    def onSearchFailed(self, _):
        self.as_freezSearchButtonS(False)

    def _populate(self):
        super(ChannelsManagementWindow, self)._populate()
        self._searchDP.init(self.as_getDataProviderS(), (self,))
        self.as_hideChannelNameInputS(IS_CHINA)

    def _dispose(self):
        if self._searchDP is not None:
            self._searchDP.fini()
            self._searchDP = None
        super(ChannelsManagementWindow, self)._dispose()
        return