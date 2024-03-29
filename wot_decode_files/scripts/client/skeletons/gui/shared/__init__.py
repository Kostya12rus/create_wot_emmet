# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/shared/__init__.py
from Event import Event
from skeletons.gui.shared.utils import IItemsRequester, requesters

class IItemsCache(requesters.IRequester):
    onSyncStarted = None
    onSyncCompleted = None

    @property
    def waitForSync(self):
        raise NotImplementedError

    @property
    def items(self):
        raise NotImplementedError

    @property
    def compatVehiclesCache(self):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def update(self, updateReason, diff=None, notify=True, callback=None):
        raise NotImplementedError

    def onDisconnected(self):
        raise NotImplementedError