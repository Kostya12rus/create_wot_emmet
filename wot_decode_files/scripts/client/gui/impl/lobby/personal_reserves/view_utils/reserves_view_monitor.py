# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/personal_reserves/view_utils/reserves_view_monitor.py
from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import LobbyHeader
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.impl.auxiliary.view_monitor import ViewMonitor
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import ViewEventType, LoadViewEvent

class ReservesViewMonitor(ViewImpl, EventSystemEntity):
    __slots__ = ('__viewMonitor', )

    def __init__(self, *args, **kwargs):
        super(ReservesViewMonitor, self).__init__(*args, **kwargs)
        self.__viewMonitor = ViewMonitor()

    def _initialize(self, *args, **kwargs):
        super(ReservesViewMonitor, self)._initialize(*args, **kwargs)
        self.addListener(ViewEventType.LOAD_VIEW, self.__onLobbyViewLoad, scope=EVENT_BUS_SCOPE.LOBBY)
        self.__viewMonitor.init(self, [
         R.views.lobby.personal_reserves.ReservesIntroView(),
         R.views.lobby.personal_reserves.ReservesConversionView()])

    def _finalize(self):
        super(ReservesViewMonitor, self)._finalize()
        self.removeListener(ViewEventType.LOAD_VIEW, self.__onLobbyViewLoad, scope=EVENT_BUS_SCOPE.LOBBY)
        self.__viewMonitor.fini()

    def __onLobbyViewLoad(self, event):
        if event.alias in LobbyHeader.TABS.ALL():
            self.destroyWindow()