# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/event/pre_queue/scheduler.py
from gui.prb_control.entities.base.scheduler import BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.periodic_battles.models import PrimeTimeStatus
from helpers import dependency
from skeletons.gui.game_control import IEventBattlesController

class EventScheduler(BaseScheduler):
    __eventBattlesCtrl = dependency.descriptor(IEventBattlesController)

    def __init__(self, entity):
        super(EventScheduler, self).__init__(entity)
        self.__isPrimeTime = False
        self.__isConfigured = False

    def init(self):
        status, _, _ = self.__eventBattlesCtrl.getPrimeTimeStatus()
        self.__isPrimeTime = status == PrimeTimeStatus.AVAILABLE
        self.__isConfigured = status != PrimeTimeStatus.NOT_SET
        self.__eventBattlesCtrl.onPrimeTimeStatusUpdated += self.__update
        self.__show(status, isInit=True)

    def fini(self):
        self.__eventBattlesCtrl.onPrimeTimeStatusUpdated -= self.__update

    def __update(self, status):
        isPrimeTime = status == PrimeTimeStatus.AVAILABLE
        isConfigured = status != PrimeTimeStatus.NOT_SET
        if isPrimeTime != self.__isPrimeTime or isConfigured != self.__isConfigured:
            self.__isPrimeTime = isPrimeTime
            self.__isConfigured = isConfigured
            self.__show(status)
            g_eventDispatcher.updateUI()

    def __show(self, status, isInit=False):
        pass