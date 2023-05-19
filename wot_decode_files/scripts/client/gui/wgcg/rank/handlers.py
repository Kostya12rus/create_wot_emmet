# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/rank/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class RankRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.RANKED_LEAGUE_POSITION: self.__getRankedPosition, 
           WebRequestDataType.RANKED_YEAR_POSITION: self.__getRankedYearPosition}
        return handlers

    def __getRankedPosition(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('rblb', 'user_ranked_position'))

    def __getRankedYearPosition(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('rblb', 'user_ranked_year_position'))