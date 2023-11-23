# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/bw_chat2/limits.py
from messenger.proto.interfaces import IProtoLimits
from messenger_common_chat2 import MESSENGER_LIMITS
from soft_exception import SoftException

class ArenaLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return MESSENGER_LIMITS.BATTLE_CHANNEL_MESSAGE_MAX_SIZE

    def getBroadcastCoolDown(self):
        return MESSENGER_LIMITS.BROADCASTS_FROM_CLIENT_COOLDOWN_SEC

    def getHistoryMaxLength(self):
        return MESSENGER_LIMITS.BATTLE_CHAT_HISTORY_ON_SERVER_MAX_LEN


class UnitLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return MESSENGER_LIMITS.UNIT_CHANNEL_MESSAGE_MAX_SIZE

    def getBroadcastCoolDown(self):
        return MESSENGER_LIMITS.BROADCASTS_FROM_CLIENT_COOLDOWN_SEC

    def getHistoryMaxLength(self):
        return MESSENGER_LIMITS.UNIT_CHAT_HISTORY_ON_SERVER_MAX_LEN


class FindUserLimits(IProtoLimits):

    def getMaxResultSize(self):
        return MESSENGER_LIMITS.FIND_USERS_BY_NAME_MAX_RESULT_SIZE

    def getRequestCooldown(self):
        return MESSENGER_LIMITS.FIND_USERS_BY_NAME_REQUEST_COOLDOWN_SEC

    def getBroadcastCoolDown(self):
        raise SoftException('This method should not be reached in this context')

    def getHistoryMaxLength(self):
        raise SoftException('This method should not be reached in this context')

    def getMessageMaxLength(self):
        raise SoftException('This method should not be reached in this context')