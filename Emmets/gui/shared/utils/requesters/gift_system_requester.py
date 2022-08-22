# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/gift_system_requester.py
import BigWorld
from adisp import async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IGiftSystemRequester

class GiftSystemRequester(AbstractSyncDataRequester, IGiftSystemRequester):

    @property
    def isHistoryReady(self):
        return bool(self.getCacheValue('isReady', False))

    @async
    def _requestCache(self, callback):
        BigWorld.player().giftSystem.getCache(lambda resID, value: self._response(resID, value, callback))