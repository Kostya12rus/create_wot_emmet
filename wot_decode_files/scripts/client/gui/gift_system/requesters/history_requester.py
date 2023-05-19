# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/requesters/history_requester.py
import BigWorld
from adisp import adisp_async
from constants import REQUEST_COOLDOWN
from gui.gift_system.requesters.base_requester import GiftSystemBaseRequester

class GiftSystemHistoryRequester(GiftSystemBaseRequester):
    __slots__ = ()

    def _getInvokeDelay(self):
        return REQUEST_COOLDOWN.SYNC_GIFTS

    @adisp_async
    def _doExternalRequest(self, reqEventIds, callback):
        BigWorld.player().giftSystem.requestGiftsHistory(reqEventIds, callback)