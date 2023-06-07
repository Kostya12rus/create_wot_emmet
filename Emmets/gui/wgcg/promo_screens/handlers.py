# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/promo_screens/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class PromoScreensRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.PROMO_GET_TEASER: self.__getTeaser, 
           WebRequestDataType.PROMO_TEASER_SHOWN: self.__sendShownTeaser, 
           WebRequestDataType.PROMO_GET_UNREAD: self.__getUnreadCount, 
           WebRequestDataType.PROMO_SEND_LOG: self.__sendActionLog}
        return handlers

    def __getTeaser(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('promo_screens', 'get_teaser'), **ctx.getAdditionalData())

    def __sendShownTeaser(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('promo_screens', 'send_teaser'), ctx.getPromoID())

    def __getUnreadCount(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('promo_screens', 'get_unread_count'))

    def __sendActionLog(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('promo_screens', 'client_promo_log'), ctx.getActionData())