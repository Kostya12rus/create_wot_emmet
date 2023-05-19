# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/stronghold_storage.py
from gui.prb_control.storages.local_storage import LocalStorage

class StrongholdStorage(LocalStorage):
    __slots__ = ('_animationIdx', )

    def __init__(self):
        super(StrongholdStorage, self).__init__()
        self._animationIdx = 0

    def fini(self):
        super(StrongholdStorage, self).fini()
        self.clear()

    def clear(self):
        super(StrongholdStorage, self).clear()
        self._animationIdx = 0

    def suspend(self):
        super(StrongholdStorage, self).suspend()
        self._animationIdx = 0

    def setActiveAnimationIdx(self, animIdx):
        self._animationIdx = animIdx

    def getActiveAnimationIdx(self):
        return self._animationIdx