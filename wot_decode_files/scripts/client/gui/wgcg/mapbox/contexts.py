# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/mapbox/contexts.py
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class MapboxProgressionCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.MAPBOX_PROGRESSION

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    @staticmethod
    def getDataObj(incomeData):
        return incomeData

    @staticmethod
    def getDefDataObj():
        return


class MapboxRequestCrewbookCtx(CommonWebRequestCtx):

    def __init__(self, crewbookItemID, waitingID=''):
        super(MapboxRequestCrewbookCtx, self).__init__(waitingID=waitingID)
        self.__crewbookItemID = crewbookItemID

    def getItemID(self):
        return self.__crewbookItemID

    def getRequestType(self):
        return WebRequestDataType.MAPBOX_CREWBOOK

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    @staticmethod
    def getDataObj(incomeData):
        return incomeData

    @staticmethod
    def getDefDataObj():
        return


class MapboxCompleteSurveyCtx(CommonWebRequestCtx):

    def __init__(self, surveyData, waitingID=''):
        super(MapboxCompleteSurveyCtx, self).__init__(waitingID=waitingID)
        self.__surveyData = surveyData

    def getSurveyData(self):
        return self.__surveyData

    def getRequestType(self):
        return WebRequestDataType.MAPBOX_SURVEY_COMPLETE

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    @staticmethod
    def getDataObj(incomeData):
        return incomeData

    @staticmethod
    def getDefDataObj():
        return


class MapboxRequestAuthorizedURLCtx(CommonWebRequestCtx):

    def __init__(self, mapURL, waitingID=''):
        super(MapboxRequestAuthorizedURLCtx, self).__init__(waitingID=waitingID)
        self.__mapURL = mapURL

    def getMapURL(self):
        return self.__mapURL

    def getRequestType(self):
        return WebRequestDataType.MAPBOX_SURVEY_URL

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    @staticmethod
    def getDataObj(incomeData):
        return incomeData

    @staticmethod
    def getDefDataObj():
        return