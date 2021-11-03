# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/local_storage.py
from gui.battle_control.arena_visitor import createByAvatar

class LocalStorage(object):
    __slots__ = ()

    def init(self):
        pass

    def fini(self):
        pass

    def swap(self):
        pass

    def release(self, *args):
        pass

    def suspend(self):
        pass

    def isModeSelected(self):
        return False

    def clear(self):
        pass

    def onAvatarBecomePlayer(self):
        pass


class SessionStorage(LocalStorage):
    __slots__ = ('_isSelected', )

    def __init__(self):
        super(SessionStorage, self).__init__()
        self._isSelected = False

    def _determineSelection(self, arenaVisitor):
        raise NotImplementedError

    def clear(self):
        self._isSelected = False

    def release(self):
        self._isSelected = True

    def suspend(self):
        self.clear()

    def isModeSelected(self):
        return self._isSelected

    def onAvatarBecomePlayer(self):
        arenaVisitor = createByAvatar()
        self._isSelected = self._determineSelection(arenaVisitor)