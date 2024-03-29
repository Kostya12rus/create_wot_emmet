# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCLoginQueue.py
from gui.Scaleform.daapi.view.meta.LoginQueueWindowMeta import LoginQueueWindowMeta
from gui.prb_control import prbDispatcherProperty
from gui.prb_control.entities.base.ctx import LeavePrbAction
from PlayerEvents import g_playerEvents
from gui.shared.events import ArgsEvent, BCLoginEvent
from gui.shared.event_bus import EVENT_BUS_SCOPE
from adisp import adisp_process

class BCLoginQueue(LoginQueueWindowMeta):

    def __init__(self, title, message, cancelLabel, _):
        super(BCLoginQueue, self).__init__()
        self.__updateData(title, message, cancelLabel)

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def onAccountBecomeNonPlayer(self):
        self.destroy()

    @adisp_process
    def onCancelClick(self):
        if self.prbDispatcher is not None:
            yield self.prbDispatcher.doLeaveAction(LeavePrbAction())
        self.fireEvent(BCLoginEvent(BCLoginEvent.CANCEL_WAITING), scope=EVENT_BUS_SCOPE.LOBBY)
        self.destroy()
        return

    def _populate(self):
        super(BCLoginQueue, self)._populate()
        self.__updateTexts()
        self.addListener(ArgsEvent.UPDATE_ARGS, self.__onUpdateArgs, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(BCLoginEvent.CLOSE_WINDOW, self.__onWindowClose, scope=EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onAccountBecomeNonPlayer += self.onAccountBecomeNonPlayer

    def _dispose(self):
        self.removeListener(ArgsEvent.UPDATE_ARGS, self.__onUpdateArgs, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(BCLoginEvent.CLOSE_WINDOW, self.__onWindowClose, scope=EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onAccountBecomeNonPlayer -= self.onAccountBecomeNonPlayer
        super(BCLoginQueue, self)._dispose()

    def __updateData(self, title, message, cancelLabel):
        self.__title = title
        self.__message = message
        self.__cancelLabel = cancelLabel

    def __updateTexts(self):
        self.as_setTitleS(self.__title)
        self.as_setMessageS(self.__message)
        self.as_setCancelLabelS(self.__cancelLabel)
        self.as_showAutoLoginBtnS(False)

    def __onUpdateArgs(self, event):
        ctx = event.ctx
        if event.alias == self.alias:
            self.__updateData(**ctx)
            self.__updateTexts()

    def __onWindowClose(self, _):
        self.destroy()