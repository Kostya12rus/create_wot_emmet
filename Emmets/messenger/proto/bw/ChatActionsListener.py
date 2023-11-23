# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/bw/ChatActionsListener.py
from ChatManager import chatManager
from debug_utils import LOG_ERROR

class ChatActionsListener(object):

    def __init__(self, responseHandlers=None):
        super(ChatActionsListener, self).__init__()
        if responseHandlers is not None:
            self._responseHandlers = responseHandlers
        else:
            self._responseHandlers = {}
        return

    def addListener(self, callback, action, cid=None):
        chatManager.subscribeChatAction(callback, action, cid)

    def removeListener(self, callback, action, cid=None):
        chatManager.unsubscribeChatAction(callback, action, cid)

    def removeAllListeners(self):
        chatManager.unsubcribeAllChatActions()

    def handleChatActionFailureEvent(self, actionResponse, chatAction):
        handler = self._responseHandlers.get(actionResponse)
        if handler is None:
            return False
        else:
            if hasattr(self, handler):
                return getattr(self, handler)(actionResponse, chatAction)
            LOG_ERROR('handleChatActionFailureEvent: response handler for response %s(%s) not registered' % (
             actionResponse, actionResponse.index()))
            return False