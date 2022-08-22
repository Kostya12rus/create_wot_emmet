# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/BaseAccountExtensionComponent.py
import BigWorld
from constants import QUEUE_TYPE

class BaseAccountExtensionComponent(BigWorld.StaticScriptComponent):
    _QUEUE_TYPE = QUEUE_TYPE.UNKNOWN

    @property
    def account(self):
        return self.entity

    @property
    def base(self):
        return self.account.base

    def getQueueType(self):
        return self._QUEUE_TYPE