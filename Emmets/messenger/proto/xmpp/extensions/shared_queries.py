# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/shared_queries.py
from messenger.proto.xmpp.extensions import PyQuery
from messenger.proto.xmpp.extensions.wg_items import WgClientExtension

class MessageQuery(PyQuery):
    __slots__ = ('_body', )

    def __init__(self, msgType, to, msgBody='', ext=None):
        super(MessageQuery, self).__init__(msgType, ext, to)
        self._body = msgBody

    def getBody(self):
        return self._body


class PresenceQuery(PyQuery):

    def __init__(self, queryType, to=''):
        super(PresenceQuery, self).__init__(queryType, WgClientExtension(), to)

    def getStatus(self):
        return ('', '')

    def isMucNsUsed(self):
        return False

    def setIgrID(self, igrID):
        if self._ext:
            self._ext.setIgrID(igrID)

    def setIgrRoomID(self, igrRoomID):
        if self._ext:
            self._ext.setIgrRoomID(igrRoomID)

    def setGameServerHost(self, host):
        if self._ext:
            self._ext.setGameServerHost(host)

    def setArenaGuiLabel(self, label):
        if self._ext:
            self._ext.setArenaGuiLabel(label)