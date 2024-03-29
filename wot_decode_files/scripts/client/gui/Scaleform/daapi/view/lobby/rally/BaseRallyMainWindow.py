# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rally/BaseRallyMainWindow.py
import BigWorld
from constants import PREBATTLE_TYPE
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.meta.BaseRallyMainWindowMeta import BaseRallyMainWindowMeta
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.entities.listener import IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.events import FocusEvent
from messenger.ext import channel_num_gen
from messenger.gui import events_dispatcher
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS

class BaseRallyMainWindow(BaseRallyMainWindowMeta, IGlobalListener):
    LEADERSHIP_NOTIFICATION_TIME = 2.5

    def __init__(self, ctx=None):
        super(BaseRallyMainWindow, self).__init__()
        self._currentView = None
        self._leadershipNotificationCallback = None
        return

    def getClientID(self):
        return channel_num_gen.getClientID4Prebattle(self.getPrbType())

    def onFocusIn(self, alias):
        self.fireEvent(FocusEvent(FocusEvent.COMPONENT_FOCUSED, {'clientID': self.getClientID()}))

    def onSourceLoaded(self):
        if self.prbDispatcher is not None and not self.prbDispatcher.getFunctionalState().isInUnit():
            self.destroy()
        return

    def isPlayerInSlot(self, databaseID=None):
        pInfo = self.prbEntity.getPlayerInfo(dbID=databaseID)
        return pInfo.isInSlot

    def getIntroViewAlias(self):
        return ''

    def getBrowserViewAlias(self, prbType):
        return ''

    def getRoomViewAlias(self, prbType):
        return ''

    def getPrbType(self):
        return PREBATTLE_TYPE.NONE

    def getPrbChatType(self):
        return PREBATTLE_TYPE.UNIT

    @property
    def chat(self):
        chat = None
        if MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT in self.components:
            chat = self.components[MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT]
        return chat

    def canGoBack(self):
        return self.prbEntity.canKeepMode()

    def onBackClick(self):
        self._doLeave(False)

    def onPrbEntitySwitched(self):
        self._loadView()

    def _populate(self):
        super(BaseRallyMainWindow, self)._populate()
        self.startGlobalListening()
        self._showLeadershipNotification()
        self._loadView()

    def _dispose(self):
        self.stopGlobalListening()
        self._currentView = None
        self._clearLeadershipNotification()
        super(BaseRallyMainWindow, self)._dispose()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT:
            events_dispatcher.rqActivateChannel(self.getClientID(), viewPy)
            return
        super(BaseRallyMainWindow, self)._onRegisterFlashComponent(viewPy, alias)

    def _onUnregisterFlashComponent(self, viewPy, alias):
        if alias == MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT:
            events_dispatcher.rqDeactivateChannel(self.getClientID())
        super(BaseRallyMainWindow, self)._onUnregisterFlashComponent(viewPy, alias)

    def _handleChannelControllerInited(self, event):
        ctx = event.ctx
        prbType = ctx.get('prbType', 0)
        if prbType is 0:
            LOG_ERROR('Prebattle type is not defined', ctx)
            return
        else:
            controller = ctx.get('controller')
            if controller is None:
                LOG_ERROR('Channel controller is not defined', ctx)
                return
            if prbType is self.getPrbChatType():
                chat = self.chat
                if chat is not None:
                    controller.setView(chat)
            return

    def _showLeadershipNotification(self):
        if self.prbEntity is not None and self.prbEntity.getShowLeadershipNotification():
            self.as_showWaitingS(backport.msgid(R.strings.waiting.prebattle.giveLeadership()), {})
            self._leadershipNotificationCallback = BigWorld.callback(self.LEADERSHIP_NOTIFICATION_TIME, self._cancelLeadershipNotification)
        return

    def _clearLeadershipNotification(self):
        if self._leadershipNotificationCallback is not None:
            BigWorld.cancelCallback(self._leadershipNotificationCallback)
            self._leadershipNotificationCallback = None
        return

    def _cancelLeadershipNotification(self):
        self._clearLeadershipNotification()
        self.prbEntity.doLeadershipNotificationShown()
        self.as_hideWaitingS()

    def _loadView(self):
        entity = self.prbEntity
        unitMgrID = entity.getID()
        prbType = entity.getEntityType()
        funcFlags = entity.getFunctionalFlags()
        if unitMgrID > 0:
            self._loadRoomView(prbType)
        elif funcFlags & FUNCTIONAL_FLAG.UNIT_BROWSER:
            self._loadBrowserView(prbType)
        elif funcFlags & FUNCTIONAL_FLAG.UNIT_INTRO:
            self._loadIntroView()
        else:
            LOG_ERROR('No view was loaded in rally window!')

    def _loadRoomView(self, prbType):
        roomAlias = self.getRoomViewAlias(prbType)
        if roomAlias:
            self._requestViewLoad(roomAlias, self.prbEntity.getID())

    def _loadIntroView(self):
        introAlias = self.getIntroViewAlias()
        if introAlias:
            self._requestViewLoad(introAlias, None)
        return

    def _loadBrowserView(self, prbType):
        browserAlias = self.getBrowserViewAlias(prbType)
        if browserAlias:
            self._requestViewLoad(browserAlias, None)
        return