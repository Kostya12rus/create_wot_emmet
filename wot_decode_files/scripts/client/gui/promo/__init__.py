# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/promo/__init__.py
from skeletons.gui.shared.promo import IPromoLogger
__all__ = ('getPromoConfig', )

def getPromoConfig(manager):
    from gui.promo.promo_logger import PromoLogger
    logger = PromoLogger()
    manager.addInstance(IPromoLogger, logger, finalizer='fini')