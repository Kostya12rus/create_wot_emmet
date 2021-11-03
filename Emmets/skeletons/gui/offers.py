# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/offers.py
import adisp
from Event import Event
from skeletons.gui import INovelty

class IOffersNovelty(INovelty):

    def saveAsSeen(self, offerId):
        raise NotImplementedError


class IOffersBannerController(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def showBanners(self):
        raise NotImplementedError

    def hideBanners(self):
        raise NotImplementedError


class IOffersDataProvider(object):
    onOffersUpdated = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def update(self, diff):
        raise NotImplementedError

    @property
    def isSynced(self):
        raise NotImplementedError

    def getReceivedGifts(self, offerID):
        raise NotImplementedError

    def isBannerSeen(self, offerID):
        raise NotImplementedError

    @adisp.async
    def isCdnResourcesReady(self, callback=None, timeout=0):
        raise NotImplementedError

    def getCdnResourcePath(self, cdnRelativePath, relative=True):
        raise NotImplementedError

    def getOffer(self, offerID):
        raise NotImplementedError

    def getOfferByToken(self, token):
        raise NotImplementedError

    def iAvailableOffers(self, onlyVisible=True):
        raise NotImplementedError

    def getAvailableOffers(self, onlyVisible=True):
        raise NotImplementedError

    def getAvailableOffersByToken(self, token):
        raise NotImplementedError

    def isOfferAvailable(self, tokenID):
        raise NotImplementedError