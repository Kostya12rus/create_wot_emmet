# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/fun_random/squad/action_handler.py
from PlayerEvents import g_playerEvents
from gui.prb_control.entities.random.squad.actions_handler import BalancedSquadActionsHandler
from helpers import dependency
from skeletons.gui.game_control import IFunRandomController, IPlatoonController

class FunRandomSquadActionsHandler(BalancedSquadActionsHandler):
    __funRandomController = dependency.descriptor(IFunRandomController)
    __platoonCtrl = dependency.descriptor(IPlatoonController)

    def __init__(self, entity):
        super(FunRandomSquadActionsHandler, self).__init__(entity)
        g_playerEvents.onDequeued += self.__onDequeued

    def clear(self):
        g_playerEvents.onDequeued -= self.__onDequeued
        super(FunRandomSquadActionsHandler, self).clear()

    def _onKickedFromQueue(self, event):
        super(FunRandomSquadActionsHandler, self)._onKickedFromQueue(event)
        if not self.__funRandomController.isInPrimeTime():
            self.__platoonCtrl.leavePlatoon(ignoreConfirmation=True)

    def __onDequeued(self, _):
        if not self.__funRandomController.isInPrimeTime():
            self.__platoonCtrl.leavePlatoon(ignoreConfirmation=True)