# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/event/loggers.py
from uilogging.base.logger import BaseLogger
from uilogging.base.mixins import TimedActionMixin
from uilogging.event.constants import FEATURE, LOG_ACTIONS

class EventLogger(TimedActionMixin, BaseLogger):

    def __init__(self, group):
        super(EventLogger, self).__init__(FEATURE, group)

    def videoStarted(self):
        self.startAction(LOG_ACTIONS.PLAY_VIDEO.value)

    def videoStopped(self, videoID):
        self.stopAction(LOG_ACTIONS.PLAY_VIDEO.value, additional_info='video_%s' % videoID)