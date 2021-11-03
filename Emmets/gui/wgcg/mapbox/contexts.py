# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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

    def __init__(self, mapName, waitingID=''):
        super(MapboxCompleteSurveyCtx, self).__init__(waitingID=waitingID)
        self.__mapName = mapName

    def getMapName(self):
        return self.__mapName

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