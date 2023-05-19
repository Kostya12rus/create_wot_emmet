# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/mapbox/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class MapboxRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.MAPBOX_PROGRESSION: self.__getMapboxProgression, 
           WebRequestDataType.MAPBOX_CREWBOOK: self.__selectCrewbook, 
           WebRequestDataType.MAPBOX_SURVEY_COMPLETE: self.__completeSurvey, 
           WebRequestDataType.MAPBOX_SURVEY_URL: self.__requestAuthorizedSurveyURL}
        return handlers

    def __getMapboxProgression(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('mapbox', 'get_mapbox_progression'))

    def __selectCrewbook(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('mapbox', 'select_mapbox_crewbook'), ctx.getItemID)

    def __completeSurvey(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('mapbox', 'complete_survey'), ctx.getSurveyData())

    def __requestAuthorizedSurveyURL(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('mapbox', 'request_authorized_survey_url'), ctx.getMapURL())