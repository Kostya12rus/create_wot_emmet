# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/e_sport/unit/actions_handler.py
from PlayerEvents import g_playerEvents
from constants import PREBATTLE_TYPE
from debug_utils import LOG_DEBUG
from gui import DialogsInterface, SystemMessages
from gui.Scaleform.daapi.view.dialogs import rally_dialog_meta
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.entities.base import vehicleAmmoCheck
from gui.prb_control.entities.base.unit.actions_handler import UnitActionsHandler
from gui.prb_control.entities.base.unit.ctx import BattleQueueUnitCtx, AutoSearchUnitCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG

class ESportActionsHandler(UnitActionsHandler):

    def __init__(self, entity):
        super(ESportActionsHandler, self).__init__(entity)
        g_playerEvents.onKickedFromUnitsQueue += self.__onKickedFromQueue

    def executeInit(self, ctx):
        prbType = self._entity.getEntityType()
        flags = self._entity.getFlags()
        g_eventDispatcher.loadUnit(prbType)
        if flags.isInIdle():
            g_eventDispatcher.setUnitProgressInCarousel(prbType, True)
        g_eventDispatcher.loadHangar()
        return FUNCTIONAL_FLAG.LOAD_WINDOW

    @vehicleAmmoCheck
    def execute(self):
        pInfo = self._entity.getPlayerInfo()
        if pInfo.isCommander():
            stats = self._entity.getStats()
            _, unit = self._entity.getUnit()
            if self._canDoAutoSearch(unit, stats):
                if self._entity.isParentControlActivated():
                    return
                if self._entity.getFlags().isDevMode():
                    DialogsInterface.showDialog(rally_dialog_meta.UnitConfirmDialogMeta(PREBATTLE_TYPE.UNIT, 'startBattle'), (lambda result: self._entity.doBattleQueue(BattleQueueUnitCtx('prebattle/battle_queue')) if result else None))
                else:
                    ctx = AutoSearchUnitCtx('prebattle/auto_search')
                    LOG_DEBUG('Unit request', ctx)
                    self._entity.doAutoSearch(ctx)
            else:
                self._sendBattleQueueRequest()
        else:
            self._entity.togglePlayerReadyAction()

    def clear(self):
        g_playerEvents.onKickedFromUnitsQueue -= self.__onKickedFromQueue
        super(ESportActionsHandler, self).clear()

    def showGUI(self):
        g_eventDispatcher.showUnitWindow(self._entity.getEntityType())

    def __onKickedFromQueue(self):
        SystemMessages.pushI18nMessage('#system_messages:arena_start_errors/prb/kick/timeout', type=SystemMessages.SM_TYPE.Warning)