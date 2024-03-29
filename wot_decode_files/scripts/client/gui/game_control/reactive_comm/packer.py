# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/reactive_comm/packer.py
import typing, cbor
from gui.game_control.reactive_comm.constants import SubscriptionServerStatus
if typing.TYPE_CHECKING:
    from gui.game_control.reactive_comm.constants import SubscriptionCommand

class ServiceMessage(object):
    __slots__ = ('cid', 'channel', 'status', 'seqid', 'data')

    def __init__(self, cid=None, channel='', status='', seqid=None, data=None, **_):
        super(ServiceMessage, self).__init__()
        self.cid = cid
        self.channel = channel
        self.status = SubscriptionServerStatus.fromString(status)
        self.seqid = seqid
        self.data = data

    @property
    def isStatusReceived(self):
        return self.channel and self.status

    @property
    def isMessageReceived(self):
        return self.cid is not None and self.data is not None

    @property
    def isValid(self):
        return self.isStatusReceived or self.isMessageReceived


def packCommand(channel, command):
    result = cbor.dumps({'channel': channel, 
       'cmd': command.value})
    return result


def unpackMessage(payload):
    raw = cbor.loads(payload)
    if not isinstance(raw, dict):
        raw = {}
    return ServiceMessage(**raw)