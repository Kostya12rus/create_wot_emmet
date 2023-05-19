# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/relogin_controller.py
from debug_utils import LOG_DEBUG
from helpers import dependency
from skeletons.gui.game_control import IReloginController
from skeletons.helpers.statistics import IStatisticsCollector

class ReloginController(IReloginController):
    statsCollector = dependency.descriptor(IStatisticsCollector)

    def __init__(self):
        super(ReloginController, self).__init__()
        self.__reloginChain = None
        self.__reloginStoppedHandler = None
        return

    def fini(self):
        self.__clearReloginChain()
        super(ReloginController, self).fini()

    def doRelogin(self, peripheryID, onStoppedHandler=None, extraChainSteps=None):
        from gui.shared import actions
        LOG_DEBUG('Attempt to relogin to the another periphery', peripheryID)
        chain = [
         actions.LeavePrbModalEntity(),
         actions.DisconnectFromPeriphery(loginViewPreselectedPeriphery=peripheryID),
         actions.ConnectToPeriphery(peripheryID)]
        if extraChainSteps is not None:
            chain += extraChainSteps
        self.__reloginStoppedHandler = onStoppedHandler
        self.__reloginChain = actions.ActionsChain(chain)
        self.__reloginChain.onStopped += self.__onReloginStopped
        self.__reloginChain.start()
        return

    def __onReloginStopped(self, isCompleted):
        if self.__reloginStoppedHandler is not None:
            self.__reloginStoppedHandler(isCompleted)
        self.statsCollector.needCollectSystemData(True)
        LOG_DEBUG('Relogin finished', isCompleted)
        return

    def __clearReloginChain(self):
        if self.__reloginChain is not None:
            self.__reloginChain.onStopped -= self.__onReloginStopped
            self.__reloginChain.stop()
            self.__reloginChain = None
            self.__reloginStoppedHandler = None
        return