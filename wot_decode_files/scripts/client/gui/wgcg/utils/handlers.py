# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/utils/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class UtilsRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.SPA_GET_ACCOUNT_ATTRIBUTE: self.__getAccountAttributeByPrefix, 
           WebRequestDataType.PLATFORM_FETCH_PRODUCT_LIST: self.__fetchProductList, 
           WebRequestDataType.PLATFORM_GET_USER_SUBSCRIPTIONS: self.__getUserSubscriptions}
        return handlers

    def __getAccountAttributeByPrefix(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('spa', 'get_account_attribute_by_prefix'), ctx.getRequestedAttr())

    def __fetchProductList(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('agate', 'agate_v4_fetch_product_list_state'), ctx.getParams())

    def __getUserSubscriptions(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('agate', 'agate_v6_get_user_subscriptions2'), ctx.getParams())