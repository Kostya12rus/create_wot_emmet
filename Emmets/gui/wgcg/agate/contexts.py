# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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