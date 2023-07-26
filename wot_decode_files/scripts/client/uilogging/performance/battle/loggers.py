# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/performance/battle/loggers.py
import logging, typing
from helpers import dependency
from skeletons.helpers.statistics import IStatisticsCollector
from uilogging.base.logger import _BaseLogger as Logger
from uilogging.constants import DEFAULT_LOGGER_NAME
from uilogging.performance.battle.constants import Features, Groups, LogActions
from uilogging.helpers import getClientSessionID
from wotdecorators import noexcept
if typing.TYPE_CHECKING:
    from uilogging.types import GroupType, PartnerIdType
_logger = logging.getLogger(DEFAULT_LOGGER_NAME)

class _BaseBattleMetricsLogger(Logger):
    __slots__ = ()

    def __init__(self, group):
        super(_BaseBattleMetricsLogger, self).__init__(Features.METRICS, group)

    @noexcept
    def log(self, data, partnerID=None, sessionID=''):
        if not isinstance(data, dict):
            _logger.error('Wrong metrics data type: [dict != %s].', type(data))
            return
        if data:
            super(_BaseBattleMetricsLogger, self)._log(LogActions.SPACE_DONE, partnerID=partnerID, session_id=sessionID, **data)
        else:
            _logger.error('%s stats are empty.', self._feature)


class _ClientSessionLogger(_BaseBattleMetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(_ClientSessionLogger, self).__init__(Groups.SESSION)


class _ClientSystemLogger(_BaseBattleMetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(_ClientSystemLogger, self).__init__(Groups.SYSTEM)


class BattleMetricsLogger(object):
    __slots__ = ('_loggers', '_defaultLogger')
    statsCollector = dependency.descriptor(IStatisticsCollector)

    def __init__(self):
        self._loggers = {Groups.SESSION.value: _ClientSessionLogger(), 
           Groups.SYSTEM.value: _ClientSystemLogger()}
        self._defaultLogger = self._loggers[Groups.SYSTEM.value]

    def initialize(self):
        self._defaultLogger.ensureSession()

    @noexcept
    def log(self):
        _logger.debug('Battle metrics requested.')
        if self._defaultLogger.disabled:
            return
        data = self.statsCollector.getStatistics()
        if not data:
            _logger.error('Battle stats are empty.')
            return
        diff = set(data) ^ set(self._loggers)
        if diff:
            _logger.error('Difference in loggers and received metrics groups: %s.', diff)
            return
        clientSessionID = getClientSessionID()
        for group, stats in data.iteritems():
            if stats:
                self._loggers[group].log(stats, sessionID=clientSessionID)