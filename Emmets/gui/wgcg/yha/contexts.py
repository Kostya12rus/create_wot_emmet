# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/yha/contexts.py
import typing
from gui.clans import items
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType
from shared_utils import makeTupleByDict, first

class YhaVideoCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.YHA_VIDEO

    def isAuthorizationRequired(self):
        return False

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    @classmethod
    def getDataObj(cls, incomeData):
        if incomeData:
            data = first(incomeData.get('data', ()), {})
            return makeTupleByDict(items.YhaVideoData, data)
        return cls.getDefDataObj()

    @staticmethod
    def getDefDataObj():
        return items.YhaVideoData()