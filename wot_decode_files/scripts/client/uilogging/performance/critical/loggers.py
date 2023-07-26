# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/performance/critical/loggers.py
import BigWorld, logging
from uilogging.base.logger import _BaseLogger as Logger
from uilogging.constants import DEFAULT_LOGGER_NAME
from uilogging.performance.critical.constants import Features, Groups, LogActions
from uilogging.helpers import getClientSessionID
from wotdecorators import noexcept
_logger = logging.getLogger(DEFAULT_LOGGER_NAME)

class MemoryCriticalLogger(Logger):
    __slots__ = ()

    def __init__(self):
        super(MemoryCriticalLogger, self).__init__(Features.MEMORY_CRITICAL, Groups.EVENT)

    def initialize(self):
        self.ensureSession()

    @noexcept
    def log(self, sessionStartedAt=0):
        _logger.debug('Critical memory metrics requested.')
        if self.disabled:
            return
        self.ensureSession()
        data = BigWorld.collectLastMemoryCriticalEvent()
        sessionID = getClientSessionID()
        if data:
            self._logImmediately(LogActions.MEMORY_CRITICAL_EVENT, session_id=sessionID, started_at=sessionStartedAt, **data)
        else:
            _logger.error('Memory critical metrics are empty')