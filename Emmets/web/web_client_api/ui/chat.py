# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/chat.py
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.storage import storage_getter
from web.web_client_api import W2CSchema, Field, w2c
from web.web_client_api.common import SPA_ID_TYPES

class _OpenChatSchema(W2CSchema):
    user_id = Field(required=True, type=SPA_ID_TYPES)
    user_name = Field(required=True, type=basestring)


class ChatWebApiMixin(object):

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    @storage_getter('users')
    def usersStorage(self):
        return

    @w2c(_OpenChatSchema, 'chat_window')
    def openChat(self, cmd):
        receiver = self.usersStorage.getUser(cmd.user_id)
        if receiver and not receiver.isIgnored():
            self.proto.contacts.createPrivateChannel(cmd.user_id, cmd.user_name.encode('utf-8'))