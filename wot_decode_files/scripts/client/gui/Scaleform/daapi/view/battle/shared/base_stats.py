# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/base_stats.py
from gui.Scaleform.daapi.view.meta.StatsBaseMeta import StatsBaseMeta
from gui.shared import events, EVENT_BUS_SCOPE
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class StatsBase(StatsBaseMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    @property
    def hasTabs(self):
        return False

    def acceptSquad(self, sessionID):
        self.sessionProvider.invitations.accept(sessionID)

    def addToSquad(self, sessionID):
        self.sessionProvider.invitations.send(sessionID)

    def onToggleVisibility(self, isVisible):
        self._onToggleVisibility(isVisible)

    def _populate(self):
        self.addListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(StatsBase, self)._populate()

    def _dispose(self):
        self.__invitations = None
        self.removeListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(StatsBase, self)._dispose()
        return

    def _onToggleVisibility(self, isVisible):
        pass

    def __handleShowCursor(self, _):
        self.as_setIsInteractiveS(True)

    def __handleHideCursor(self, _):
        self.as_setIsInteractiveS(False)