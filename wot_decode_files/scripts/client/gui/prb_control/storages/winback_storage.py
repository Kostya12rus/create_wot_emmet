# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/winback_storage.py
from constants import QUEUE_TYPE
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IWinbackController

class WinbackStorage(SessionStorage):
    __winbackController = dependency.descriptor(IWinbackController)

    def isModeSelected(self):
        return super(WinbackStorage, self).isModeSelected() and self.isModeAvailable()

    def isModeAvailable(self):
        return self.__winbackController.isModeAvailable()

    def shouldBeSelectedByDefault(self):
        return self.isModeAvailable()

    def getQueueTypeToReplace(self):
        return QUEUE_TYPE.RANDOMS

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.isWinback()