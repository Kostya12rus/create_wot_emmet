# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/shared/promo.py


class IPromoLogger(object):

    def logAction(self, **kwargs):
        raise NotImplementedError

    def logTeaserAction(self, teaserData, **kwargs):
        raise NotImplementedError

    def getLoggingFuture(self, teaserData=None, **kwargs):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError