# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/bw/search_processors.py
import chat_shared
from constants import CHANNEL_SEARCH_RESULTS_LIMIT
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.bw import cooldown
from messenger.proto.search_processor import SearchProcessor
from soft_exception import SoftException

class SearchChannelsProcessor(SearchProcessor):

    def init(self):
        super(SearchChannelsProcessor, self).init()
        channels = self.proto.channels
        channels.onRequestChannelsComplete += self.__cm_onSearchTokenComplete
        channels.onFindChannelsFailed += self.__cm_onSearchTokenFailed
        channels.onChannelExcludeFromSearch += self.__cm_onChannelExcludeFromSearch

    @proto_getter(PROTO_TYPE.BW)
    def proto(self):
        return

    def fini(self):
        super(SearchChannelsProcessor, self).fini()
        channels = self.proto.channels
        channels.onRequestChannelsComplete -= self.__cm_onSearchTokenComplete
        channels.onFindChannelsFailed -= self.__cm_onSearchTokenFailed
        channels.onChannelExcludeFromSearch -= self.__cm_onChannelExcludeFromSearch

    def isInCooldown(self):
        chatCommand = self.getChatCommand()
        result = False
        message = ''
        if cooldown.isOperationInCooldownEx(chatCommand):
            result = True
            message = cooldown.getOperationInCooldownMsg(chatCommand, cooldown.getOperationCooldownPeriodEx(chatCommand))
        return (
         result, message)

    def find(self, token, **kwargs):
        result, message = self.isInCooldown()
        if result:
            self._onSearchFailed(message)
            return
        self._lastRequestID = self._makeRequestID()
        self.proto.channels.findChannels(token, requestID=self._lastRequestID)

    def getChatCommand(self):
        return chat_shared.CHAT_COMMANDS.findChatChannels.name()

    def getSearchResultLimit(self):
        return CHANNEL_SEARCH_RESULTS_LIMIT

    def getSearchCoolDown(self):
        raise SoftException('This method should not be reached in this context')

    def __cm_onSearchTokenComplete(self, requestID, result):
        self._onSearchTokenComplete(requestID, result)

    def __cm_onSearchTokenFailed(self, requestID, actionResponse, data):
        if self._lastRequestID == requestID:
            if actionResponse == chat_shared.CHAT_RESPONSES.commandInCooldown:
                reason = cooldown.getOperationInCooldownMsg(self.getChatCommand(), data.get('cooldownPeriod', -1))
                self._onSearchFailed(reason)

    def __cm_onChannelExcludeFromSearch(self, channel):
        self._onExcludeFromSearch(channel)