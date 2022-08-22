# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/agate/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class AgateRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.AGATE_INVENTORY_ENTITLEMENTS: self.__getInventoryEntitlements}
        return handlers

    def __getInventoryEntitlements(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('agate', 'get_inventory_entitlements'), entitlement_codes=ctx.getEntitlementCodes())