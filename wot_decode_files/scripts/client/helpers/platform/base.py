# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/platform/base.py
from Event import EventManager, Event
from skeletons.helpers.platform import IPublishPlatform

class BasePublishPlatform(IPublishPlatform):
    __slots__ = ('__eventMgr', 'onPayment', 'onOverlay')

    def __init__(self):
        super(BasePublishPlatform, self).__init__()
        self.__eventMgr = EventManager()
        self.onPayment = Event(self.__eventMgr)
        self.onOverlay = Event(self.__eventMgr)

    def init(self):
        pass

    def fini(self):
        self.__eventMgr.clear()

    def isInited(self):
        return False

    def isConnected(self):
        return False