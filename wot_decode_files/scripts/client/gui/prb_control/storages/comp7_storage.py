# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/comp7_storage.py
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7Storage(SessionStorage):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def isModeSelected(self):
        return self.__comp7Controller.isEnabled() and not self.__comp7Controller.isFrozen() and super(Comp7Storage, self).isModeSelected()

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.isComp7Battle()