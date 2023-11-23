# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/helpers/platform.py
import typing
if typing.TYPE_CHECKING:
    from Event import Event

class IPublishPlatform(object):
    onPayment = None
    onOverlay = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def isInited(self):
        raise NotImplementedError

    def isConnected(self):
        raise NotImplementedError