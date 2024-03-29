# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/agate/contexts.py
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class InventoryEntitlementsCtx(CommonWebRequestCtx):
    __slots__ = ('__entitlementCodes', )

    def __init__(self, entitlementCodes=(), waitingID=''):
        super(InventoryEntitlementsCtx, self).__init__(waitingID)
        self.__entitlementCodes = entitlementCodes

    def getRequestType(self):
        return WebRequestDataType.AGATE_INVENTORY_ENTITLEMENTS

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getEntitlementCodes(self):
        return self.__entitlementCodes

    @staticmethod
    def getDataObj(incomeData):
        return incomeData


class AgateGetInventoryEntitlementsCtx(CommonWebRequestCtx):
    __slots__ = ('__entitlementsFilter', )

    def __init__(self, entitlementsFilter, waitingID=''):
        self.__entitlementsFilter = entitlementsFilter
        super(AgateGetInventoryEntitlementsCtx, self).__init__(waitingID=waitingID)

    def getRequestType(self):
        return WebRequestDataType.AGATE_GET_INVENTORY_ENTITLEMENTS_V5

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getEntitlementsFilter(self):
        return self.__entitlementsFilter

    @staticmethod
    def getDataObj(incomeData):
        return incomeData

    @staticmethod
    def getDefDataObj():
        return