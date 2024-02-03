# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/shop/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class ShopRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.SHOP_INVENTORY_ENTITLEMENTS: self.__getInventoryEntitlements, 
           WebRequestDataType.SHOP_GET_STOREFRONT_PRODUCTS: self.__getStorefrontProducts, 
           WebRequestDataType.SHOP_BUY_STOREFRONT_PRODUCTS: self.__buyStorefrontProducts}
        return handlers

    def __getInventoryEntitlements(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('shop', 'get_inventory_entitlements'), entitlement_codes=ctx.getEntitlementCodes())

    def __getStorefrontProducts(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('shop', 'get_storefront_products'), storefront=ctx.getStorefront())

    def __buyStorefrontProducts(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('shop', 'buy_storefront_products'), storefront=ctx.getStorefront(), productCode=ctx.getProductCode(), requestData=ctx.getData())