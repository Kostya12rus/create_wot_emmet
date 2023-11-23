# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/states/handlers/milestones.py
import time, typing, Event
from PlayerEvents import g_playerEvents
from bootcamp.BootCampEvents import g_bootcampEvents
from constants import IS_DEVELOPMENT
from gui.game_loading import loggers
from gui.game_loading.resources.consts import MilestonesTypes, Milestones
from shared_utils import first
if typing.TYPE_CHECKING:
    from gui.game_loading.state_machine.models import LoadingMilestoneModel
_logger = loggers.getStatesLogger()

class MilestonesHandler(object):
    __slots__ = ('onMilestoneReached', 'onMilestoneTypeChanged', '_milestonesSettings',
                 '_milestones', '_milestone', '_time')

    def __init__(self, milestonesSettings):
        self._milestone = None
        self._milestonesSettings = milestonesSettings
        self._time = 0
        self.onMilestoneReached = Event.SafeEvent()
        self.onMilestoneTypeChanged = Event.SafeEvent()
        self.init()
        return

    def init(self):
        self._chooseMilestonesType(MilestonesTypes.CONNECTION)

    def start(self):
        self._time = time.time()
        g_playerEvents.onLoadingMilestoneReached += self._onLoadingMilestoneReached
        g_playerEvents.onAccountBecomePlayer += self._onStandardLoading
        g_bootcampEvents.onBootcampBecomePlayer += self._onBootcampLoading

    def stop(self):
        g_playerEvents.onLoadingMilestoneReached -= self._onLoadingMilestoneReached
        g_playerEvents.onAccountBecomePlayer -= self._onStandardLoading
        g_bootcampEvents.onBootcampBecomePlayer -= self._onBootcampLoading
        self.onMilestoneReached.clear()
        self.onMilestoneTypeChanged.clear()

    def getCurrentMilestone(self):
        return self._milestone

    def _onStandardLoading(self):
        self._chooseMilestonesType(MilestonesTypes.STANDARD)

    def _onBootcampLoading(self):
        self._chooseMilestonesType(MilestonesTypes.BOOTCAMP)

    def _chooseMilestonesType(self, milestonesType):
        if milestonesType not in self._milestonesSettings:
            _logger.error('Unknown milestones type: %s', milestonesType)
            return
        self._milestones = self._milestonesSettings[milestonesType]
        self._milestone = first(sorted(self._milestones.values(), key=(lambda m: m.percent)))
        _logger.debug('[%s] New milestone type was chosen: %s. Milestone applied: %s.', self, milestonesType, self._milestone.name)
        self.onMilestoneTypeChanged(self._milestone)

    def _onLoadingMilestoneReached(self, milestoneName):
        _logger.debug('[%s] New milestone was reached: %s.', self, milestoneName)
        newMilestone = self._milestones.get(milestoneName)
        if newMilestone is None:
            _logger.debug('[%s] Unknown milestone: %s. Available: %s', self, milestoneName, self._milestones)
            return
        else:
            if self._milestone is not None and self._milestone.percent >= newMilestone.percent:
                _logger.debug('[%s] Try to apply previous milestone: %s %s', self, self._milestone, newMilestone)
                return
            self._milestone = newMilestone
            self.onMilestoneReached(newMilestone)
            if IS_DEVELOPMENT:
                self._logTimeDelay()
            return

    def _logTimeDelay(self):
        current = time.time()
        _logger.debug('[%s]: Got %.2f delay between milestones.', self._milestone.name, current - self._time)
        self._time = current

    def __repr__(self):
        return ('{}').format(self.__class__.__name__)


class StatusTextMilestonesHandler(MilestonesHandler):
    pass


class ProgressBarMilestonesHandler(MilestonesHandler):
    pass