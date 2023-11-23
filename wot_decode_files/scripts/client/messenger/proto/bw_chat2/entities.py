# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/bw_chat2/entities.py
from constants import PREBATTLE_TYPE_NAMES
from messenger.ext import channel_num_gen
from messenger.m_constants import PROTO_TYPE
from messenger.proto.bw_chat2.wrappers import ChannelProtoData, CHAT_TYPE
from messenger.proto.entities import ChannelEntity, MemberEntity

class _BWChannelEntity(ChannelEntity):

    def __init__(self, chatType, settings):
        super(_BWChannelEntity, self).__init__(ChannelProtoData(chatType, settings))
        self._isJoined = True

    def getProtoType(self):
        return PROTO_TYPE.BW_CHAT2

    def isSystem(self):
        return True


class BWBattleChannelEntity(_BWChannelEntity):

    def __init__(self, settings):
        super(BWBattleChannelEntity, self).__init__(CHAT_TYPE.ARENA, settings)

    def getID(self):
        return channel_num_gen.getClientID4BattleChannel(self.getName())

    def getName(self):
        return self.getProtoData().settings.name

    def getFullName(self):
        return self.getName()

    def isBattle(self):
        return True


class BWUnitChannelEntity(_BWChannelEntity):

    def __init__(self, settings, prbType):
        super(BWUnitChannelEntity, self).__init__(CHAT_TYPE.UNIT, settings)
        self._prbType = prbType

    def getID(self):
        return channel_num_gen.getClientID4Prebattle(self._prbType)

    def getName(self):
        return ('#chat:channels/{0}').format(PREBATTLE_TYPE_NAMES[self._prbType].lower())

    def getFullName(self):
        return self.getName()

    def isPrebattle(self):
        return True

    def getPrebattleType(self):
        return self._prbType


class BWMemberEntity(MemberEntity):

    def __init__(self, jid, nickName, status=None):
        super(BWMemberEntity, self).__init__(jid, nickName, status)

    def getDatabaseID(self):
        return self.getID()

    def getProtoType(self):
        return PROTO_TYPE.BW_CHAT2