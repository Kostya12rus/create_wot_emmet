# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/promo_screens/contexts.py
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.promo_screens.parsers import PromoDataParser
from gui.wgcg.settings import WebRequestDataType

class PromoGetTeaserRequestCtx(CommonWebRequestCtx):

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    @staticmethod
    def getDataObj(incomeData):
        return PromoDataParser.parse(incomeData)

    def isCaching(self):
        return False

    def getRequestType(self):
        return WebRequestDataType.PROMO_GET_TEASER


class PromoSendTeaserShownRequestCtx(CommonWebRequestCtx):

    def __init__(self, promoID, waitingID=''):
        super(PromoSendTeaserShownRequestCtx, self).__init__(waitingID=waitingID)
        self.__promoID = promoID

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def getPromoID(self):
        return self.__promoID

    def isCaching(self):
        return False

    def getRequestType(self):
        return WebRequestDataType.PROMO_TEASER_SHOWN


class PromoGetUnreadCountRequestCtx(CommonWebRequestCtx):

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getRequestType(self):
        return WebRequestDataType.PROMO_GET_UNREAD

    @staticmethod
    def getCount(response):
        return response.getData().get('unread', 0)


class PromoSendActionLogCtx(CommonWebRequestCtx):

    def __init__(self, data, waitingID=''):
        super(PromoSendActionLogCtx, self).__init__(waitingID=waitingID)
        self.__data = data

    def isAuthorizationRequired(self):
        return False

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getRequestType(self):
        return WebRequestDataType.PROMO_SEND_LOG

    def getActionData(self):
        return self.__data