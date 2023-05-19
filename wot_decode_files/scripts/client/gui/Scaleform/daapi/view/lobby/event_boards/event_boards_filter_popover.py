# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_filter_popover.py
from gui.Scaleform.daapi.view.meta.EventBoardsResultFilterPopoverViewMeta import EventBoardsResultFilterPopoverViewMeta
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS
from gui.shared.utils.functions import makeTooltip
from .event_boards_vos import makeFiltersVO

class EventBoardsFilterPopover(EventBoardsResultFilterPopoverViewMeta):

    def __init__(self, ctx=None):
        super(EventBoardsFilterPopover, self).__init__(ctx)
        data = ctx.get('data')
        self.caller = data.caller if data else None
        self.eventID = data.eventID if data else None
        self.__onChangeFilter = None
        return

    def changeFilter(self, lid):
        self.__onChangeFilter(int(lid))

    def onWindowClose(self):
        self.destroy()

    def setData(self, eventData, onApply, leaderboardID=None):
        self.__onChangeFilter = onApply
        eventType = eventData.getType()
        leaderboards = eventData.getLeaderboards()
        if leaderboardID is None:
            leaderboardID = leaderboards[0][0]
        data = {'filters': makeFiltersVO(eventType, leaderboards, leaderboardID), 
           'tooltip': makeTooltip(EVENT_BOARDS.POPOVER_BUTTONS_RATING, ('#event_boards:popover/tooltip/{}').format(eventType))}
        self.as_setInitDataS(data)
        return