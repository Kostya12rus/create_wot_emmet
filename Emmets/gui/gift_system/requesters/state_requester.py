# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/requesters/state_requester.py
from adisp import adisp_async, adisp_process
from gui.gift_system.requesters.base_requester import GiftSystemBaseRequester
from gui.wgcg.gift_system.contexts import GiftSystemStateCtx
from helpers import dependency
from helpers.time_utils import ONE_MINUTE
from skeletons.gui.web import IWebController
_WGCG_AVAILABILITY = 2
_WGGG_AVAILABILITY = ONE_MINUTE

class GiftSystemWebStateRequester(GiftSystemBaseRequester):
    __slots__ = ()
    __webController = dependency.descriptor(IWebController)

    def _getInvokeDelay(self):
        if self.__webController.isAvailable():
            return _WGGG_AVAILABILITY
        return _WGCG_AVAILABILITY

    @adisp_async
    @adisp_process
    def _doExternalRequest(self, reqEventIds, callback):
        if not self.__webController.isAvailable():
            callback((False, {}))
            return
        requestCtx = GiftSystemStateCtx(reqEventIds)
        result = yield self.__webController.sendRequest(requestCtx)
        callback((result.isSuccess(), requestCtx.getDataObj(result.data) if result.isSuccess() else {}))