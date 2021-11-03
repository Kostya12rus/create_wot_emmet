# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/offers/__init__.py
from gui.offers.offers_banner_controller import OffersBannerController
from gui.offers.data_provider import OffersDataProvider
from gui.offers.offers_novelty import OffersNovelty
from skeletons.gui.offers import IOffersNovelty, IOffersBannerController, IOffersDataProvider

def getOffersConfig(manager):

    def _create():
        instance = OffersNovelty()
        instance.init()
        return instance

    manager.addRuntime(IOffersNovelty, _create, finalizer='fini')
    offersPrv = OffersDataProvider()
    offersPrv.init()
    manager.addInstance(IOffersDataProvider, offersPrv, finalizer='fini')
    bannerCtrl = OffersBannerController()
    bannerCtrl.init()
    manager.addInstance(IOffersBannerController, bannerCtrl, finalizer='fini')