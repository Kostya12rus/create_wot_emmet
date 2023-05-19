# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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