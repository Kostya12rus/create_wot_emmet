# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/advent_calendar/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class AdventCalendarRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.ADVENT_CALENDAR_FETCH_HERO_TANK_INFO: self.__fetchHeroTankInfo}
        return handlers

    def __fetchHeroTankInfo(self, ctx, callback):
        reqCtx = self._requester.doRequestEx(ctx, callback, ('advent_calendar', 'advent_calendar_fetch_hero_tank_info'))
        return reqCtx