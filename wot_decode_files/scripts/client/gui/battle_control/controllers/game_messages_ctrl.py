# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/game_messages_ctrl.py
import weakref
from collections import namedtuple
from PlayerEvents import g_playerEvents
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.view_components import IViewComponentsController
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class PlayerMessageData(namedtuple('playerMessageData', ('messageType', 'length', 'priority', 'msgData'))):

    def getDict(self):
        return self._asdict()


class GameMessagesController(IViewComponentsController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, setup):
        super(GameMessagesController, self).__init__()
        self.__arenaVisitor = weakref.proxy(setup.arenaVisitor)
        self.__ui = None
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.GAME_MESSAGES_PANEL

    def startControl(self):
        if self.__arenaVisitor.hasGameEndMessage():
            g_playerEvents.onRoundFinished += self.__onRoundFinished

    def setViewComponents(self, component):
        self.__ui = component

    def clearViewComponents(self):
        self.__ui = None
        return

    def stopControl(self):
        if self.__arenaVisitor.hasGameEndMessage():
            g_playerEvents.onRoundFinished -= self.__onRoundFinished
        self.__arenaVisitor = None
        return

    def __onRoundFinished(self, winningTeam, reason, extraData):
        if self.__ui:
            self.__ui.sendEndGameMessage(winningTeam, reason, extraData)


def createGameMessagesController(setup):
    return GameMessagesController(setup)