# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/seniority_awards/loggers.py
from uilogging.base.logger import MetricsLogger
from uilogging.constants import CommonLogActions
from uilogging.seniority_awards.constants import FEATURE, SeniorityAwardsLogItem, SeniorityAwardsLogParentScreen

class SeniorityAwardsLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(SeniorityAwardsLogger, self).__init__(FEATURE)

    def handleNotificationAction(self):
        self.log(action=CommonLogActions.CLICK, item=SeniorityAwardsLogItem.NOTIFICATION, parentScreen=SeniorityAwardsLogParentScreen.HANGAR)