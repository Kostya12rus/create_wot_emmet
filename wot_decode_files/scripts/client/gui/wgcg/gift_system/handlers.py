# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/gift_system/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class GiftSystemRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.GIFT_SYSTEM_STATE: self.__getGiftSystemState, 
           WebRequestDataType.GIFT_SYSTEM_POST_GIFT: self.__postGiftSystemGift}
        return handlers

    def __getGiftSystemState(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('gifts', 'get_gift_system_state'), ctx.getReqEventIds())

    def __postGiftSystemGift(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('gifts', 'post_gift_system_gift'), ctx.getEntitlementCode(), ctx.getReceiverID(), ctx.getMetaInfo())