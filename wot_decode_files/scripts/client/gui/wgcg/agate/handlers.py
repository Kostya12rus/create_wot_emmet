# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/agate/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class AgateRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.AGATE_INVENTORY_ENTITLEMENTS: self.__getInventoryEntitlements, 
           WebRequestDataType.AGATE_GET_INVENTORY_ENTITLEMENTS_V5: self.__getInventoryEntitlementsV5}
        return handlers

    def __getInventoryEntitlements(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('agate', 'get_inventory_entitlements'), entitlement_codes=ctx.getEntitlementCodes())

    def __getInventoryEntitlementsV5(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('agate', 'get_inventory_entitlements_v5'), entitlementsFilter=ctx.getEntitlementsFilter())