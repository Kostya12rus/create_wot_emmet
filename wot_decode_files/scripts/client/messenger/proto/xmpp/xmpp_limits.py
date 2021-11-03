# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/xmpp_limits.py
from messenger.proto.interfaces import IUserSearchLimits, IProtoLimits
from messenger.proto.xmpp.xmpp_constants import USER_SEARCH_LIMITS, MESSAGE_LIMIT

class FindUserSearchLimits(IUserSearchLimits):

    def getMaxResultSize(self):
        return USER_SEARCH_LIMITS.FIND_USERS_BY_NAME_MAX_RESULT_SIZE

    def getRequestCooldown(self):
        return USER_SEARCH_LIMITS.FIND_USERS_BY_NAME_REQUEST_COOLDOWN_SEC


class MessageLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return MESSAGE_LIMIT.MESSAGE_MAX_SIZE

    def getBroadcastCoolDown(self):
        return MESSAGE_LIMIT.COOLDOWN

    def getHistoryMaxLength(self):
        return MESSAGE_LIMIT.HISTORY_MAX_LEN