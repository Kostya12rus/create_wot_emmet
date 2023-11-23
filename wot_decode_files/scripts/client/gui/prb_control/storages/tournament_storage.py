# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/tournament_storage.py
from gui.prb_control.storages.local_storage import LocalStorage

class TournamentStorage(LocalStorage):
    __slots__ = ('_animationIdx', )

    def __init__(self):
        super(TournamentStorage, self).__init__()
        self._animationIdx = 0

    def fini(self):
        super(TournamentStorage, self).fini()
        self.clear()

    def clear(self):
        super(TournamentStorage, self).clear()
        self._animationIdx = 0

    def suspend(self):
        super(TournamentStorage, self).suspend()
        self._animationIdx = 0

    def setActiveAnimationIdx(self, animIdx):
        self._animationIdx = animIdx

    def getActiveAnimationIdx(self):
        return self._animationIdx