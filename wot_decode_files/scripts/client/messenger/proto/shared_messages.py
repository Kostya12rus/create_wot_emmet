# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/shared_messages.py
from messenger.proto.interfaces import IChatMessage

class ACTION_MESSAGE_TYPE(object):
    PLAYER = 0
    WARNING = 1
    ERROR = 2


class ClientActionMessage(IChatMessage):

    def __init__(self, msg=None, type_=ACTION_MESSAGE_TYPE.PLAYER):
        super(ClientActionMessage, self).__init__()
        self.__message = msg
        self.__type = type_

    def setMessage(self, msg):
        self.__message = msg

    def getMessage(self):
        return self.__message

    def getType(self):
        return self.__type