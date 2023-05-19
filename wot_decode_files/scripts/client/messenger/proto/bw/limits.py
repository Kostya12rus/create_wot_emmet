# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/bw/limits.py
from constants import CHAT_MESSAGE_MAX_LENGTH, CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE
from messenger.m_constants import MESSAGES_HISTORY_MAX_LEN
from messenger.proto.interfaces import IProtoLimits
from soft_exception import SoftException

class BattleLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE

    def getHistoryMaxLength(self):
        return MESSAGES_HISTORY_MAX_LEN

    def getBroadcastCoolDown(self):
        raise SoftException('This method should not be reached in this context')


class LobbyLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return CHAT_MESSAGE_MAX_LENGTH

    def getHistoryMaxLength(self):
        return MESSAGES_HISTORY_MAX_LEN

    def getBroadcastCoolDown(self):
        raise SoftException('This method should not be reached in this context')


class CHANNEL_LIMIT(object):
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 32
    PWD_MIN_LENGTH = 3
    PWD_MAX_LENGTH = 12