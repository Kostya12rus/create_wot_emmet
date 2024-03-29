# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/e_sport/unit/requester.py
import logging, time, BigWorld
from UnitBase import UNIT_ERROR
from gui.prb_control.events_dispatcher import g_eventDispatcher
from helpers import time_utils
_logger = logging.getLogger(__name__)

def _logDeprecationError():
    _logger.error('Auto search of account for e sports deprecated since Platoon 2.0.')


class UnitAutoSearchHandler(object):

    def __init__(self, entity):
        super(UnitAutoSearchHandler, self).__init__()
        self.__entity = entity
        self.__vTypeDescrs = []
        self.__isInSearch = False
        self.__hasResult = False
        self.__startSearchTime = -1
        self.__lastErrorCode = UNIT_ERROR.OK

    def init(self):
        _logDeprecationError()

    def fini(self):
        _logDeprecationError()
        self.__entity = None
        return

    def initEvents(self, listener):
        _logDeprecationError()

    def isInSearch(self):
        return self.__isInSearch

    def getTimeLeftInSearch(self):
        if self.__startSearchTime > -1:
            timeLeft = int(BigWorld.time() - self.__startSearchTime)
        else:
            timeLeft = -1
        return timeLeft

    def getAcceptDelta(self, acceptDeadlineUTC):
        if acceptDeadlineUTC:
            return max(0, int(time_utils.makeLocalServerTime(acceptDeadlineUTC) - time.time()))
        return 0

    def start(self, vTypeDescrs=None):
        _logDeprecationError()
        return False

    def stop(self):
        _logDeprecationError()
        return False

    def accept(self):
        _logDeprecationError()
        return False

    def decline(self):
        _logDeprecationError()
        return False

    def unitBrowser_onErrorReceived(self, errorCode, errorStr):
        self.__isInSearch = False
        self.__lastErrorCode = errorCode
        if errorCode != UNIT_ERROR.OK:
            for listener in self.__entity.getListenersIterator():
                listener.onUnitBrowserErrorReceived(errorCode)

        g_eventDispatcher.updateUI()