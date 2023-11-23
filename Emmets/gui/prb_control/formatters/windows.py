# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/formatters/windows.py
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class SwitchPeripheryCtx(object):

    def __init__(self, isForbidden=True):
        super(SwitchPeripheryCtx, self).__init__()
        self.__isForbidden = isForbidden

    def getHeader(self):
        raise NotImplementedError

    def getDescription(self):
        raise NotImplementedError

    def getSelectServerLabel(self):
        raise NotImplementedError

    def getApplySwitchLabel(self):
        raise NotImplementedError

    def getExtraChainSteps(self):
        raise NotImplementedError

    def getUpdateTime(self):
        return 0

    def isPeripheryAvailable(self, peripheryID):
        if self.__isForbidden:
            return peripheryID not in self._getForbiddenPeripherieIDs()
        return peripheryID in self._getAllowedPeripherieIDs()

    def _getForbiddenPeripherieIDs(self):
        raise NotImplementedError

    def _getAllowedPeripherieIDs(self):
        raise NotImplementedError


class SwitchPeripheryFortCtx(SwitchPeripheryCtx):
    lobbyContext = dependency.descriptor(ILobbyContext)

    def getHeader(self):
        return backport.msgid(R.strings.prebattle.switchPeripheryWindow.fort.header())

    def getDescription(self):
        return backport.msgid(R.strings.prebattle.switchPeripheryWindow.fort.description())

    def getSelectServerLabel(self):
        return backport.msgid(R.strings.prebattle.switchPeripheryWindow.fort.selectServerLabel())

    def getApplySwitchLabel(self):
        return backport.msgid(R.strings.prebattle.switchPeripheryWindow.fort.applySwitchLabel())

    def getExtraChainSteps(self):
        return

    def _getForbiddenPeripherieIDs(self):
        return self.lobbyContext.getServerSettings().getForbiddenSortiePeripheryIDs()