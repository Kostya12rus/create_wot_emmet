# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/hof/contexts.py
from gui.clans import items
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType
from shared_utils import makeTupleByDict

class _BaseHofRequestCtx(CommonWebRequestCtx):

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def getDataObj(self, incomeData):
        incomeData = incomeData or {}
        return makeTupleByDict(items.HofAttrs, incomeData)

    def getDefDataObj(self):
        return

    def isCaching(self):
        return False


class HofUserInfoCtx(_BaseHofRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.HOF_USER_INFO


class HofUserExcludeCtx(_BaseHofRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.HOF_USER_EXCLUDE


class HofUserRestoreCtx(_BaseHofRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.HOF_USER_RESTORE