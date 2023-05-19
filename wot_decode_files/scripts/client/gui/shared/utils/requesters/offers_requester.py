# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/offers_requester.py
import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IOffersRequester

class OffersRequester(AbstractSyncDataRequester, IOffersRequester):

    def getReceivedGifts(self, offerID):
        return self.__getOffer(offerID).get('gifts', dict())

    def isBannerSeen(self, offerID):
        return self.__getOffer(offerID).get('bannerSeen', False)

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().offers.getCache((lambda resID, value: self._response(resID, value, callback)))

    def __getOffer(self, offerID):
        return self.getCacheValue('offersData', {}).get(offerID, {})