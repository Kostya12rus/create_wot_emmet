# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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