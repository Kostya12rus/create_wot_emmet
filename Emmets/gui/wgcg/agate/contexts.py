# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/agate/contexts.py
import typing
from enum import Enum
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType
if typing.TYPE_CHECKING:
    from typing import Dict, List

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

    class _FilterKeys(Enum):
        CODE = 'code'
        TAG = 'tag'

    class _FilterOperators(Enum):
        IN = 'in'
        NOT_IN = 'not_in'
        EQ = 'eq'
        NEQ = 'neq'

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

    @classmethod
    def createFilterByTags(cls, tags):
        tagsFilter = {'key': cls._FilterKeys.TAG.value, 
           'operator': cls._FilterOperators.IN.value, 
           'value': tags}
        return {'filter': [tagsFilter]}

    @classmethod
    def createFilterByCodes(cls, codes):
        operator, value = cls.__makeRequestArgsForValues(codes)
        return {'filter': [
                    {'key': cls._FilterKeys.CODE.value, 
                       'operator': operator, 
                       'value': value}]}

    @classmethod
    def __makeRequestArgsForValues(cls, valuesList):
        if len(valuesList) > 1:
            return (cls._FilterOperators.IN.value, valuesList)
        return (cls._FilterOperators.EQ.value, valuesList[0])