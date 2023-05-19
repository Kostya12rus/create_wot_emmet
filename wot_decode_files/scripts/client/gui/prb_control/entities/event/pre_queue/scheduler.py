# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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