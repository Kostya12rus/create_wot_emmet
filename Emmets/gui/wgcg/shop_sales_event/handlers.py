# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/shop_sales_event/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class ShopSalesEventRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.SHOP_SALES_EVENT_FETCH_FAVORITES: self.__fetchFavorites}
        return handlers

    def __fetchFavorites(self, ctx, callback):
        reqCtx = self._requester.doRequestEx(ctx, callback, ('shop_sales_event', 'shop_sales_event_fetch_favorites'))
        return reqCtx