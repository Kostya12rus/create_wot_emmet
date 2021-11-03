# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/bootcamp/loggers.py
from bootcamp.Bootcamp import g_bootcamp
from helpers import dependency
from skeletons.gui.game_control import IBootcampController
from uilogging.base.logger import BaseLogger, ifUILoggingEnabled
from uilogging.base.mixins import LogOnceMixin, TimedActionMixin
from uilogging.core.core_constants import LogLevels
from uilogging.deprecated.logging_constants import FEATURES
from wotdecorators import noexcept

class BootcampLogger(TimedActionMixin, LogOnceMixin, BaseLogger):
    __bootcamp = dependency.descriptor(IBootcampController)

    def __init__(self, group):
        super(BootcampLogger, self).__init__(FEATURES.BOOTCAMP, group)

    @noexcept
    @ifUILoggingEnabled()
    def log(self, action, loglevel=LogLevels.INFO, **params):
        if 'timeSpent' in params:
            params['timeSpent'] = int(params['timeSpent'])
        params['lesson_id'] = g_bootcamp.getLessonNum()
        params['is_newbie'] = g_bootcamp.isNewbie()
        return super(BootcampLogger, self).log(action=action, loglevel=loglevel, **params)

    def logOnlyFromBootcamp(self, action, loglevel=LogLevels.INFO, **params):
        if not self.__bootcamp.isInBootcamp():
            return
        self.log(action=action, loglevel=loglevel, **params)