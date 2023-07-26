# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/collections/loggers.py
from uilogging.base.logger import MetricsLogger
from uilogging.collections.constants import FEATURE, CollectionsItem
from uilogging.constants import CommonLogActions

class CollectionsLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(CollectionsLogger, self).__init__(FEATURE)

    def handleRewardNotificationAction(self, collectionID):
        self.logOnce(action=CommonLogActions.CLICK, item=CollectionsItem.REWARD_NOTIFICATION, info=str(collectionID))

    def handleGameObjectClick(self, collectionID):
        self.log(action=CommonLogActions.CLICK, item=CollectionsItem.GAME_OBJECT, info=str(collectionID))