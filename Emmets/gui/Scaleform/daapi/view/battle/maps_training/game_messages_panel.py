# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/maps_training/game_messages_panel.py
from gui.Scaleform.daapi.view.battle.shared.game_messages_panel import GameMessagesPanel, PlayerMessageData
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS
from gui.battle_control import avatar_getter
from gui.impl import backport
from gui.impl.gen import R

class MapsTrainingGameMessagesPanel(GameMessagesPanel):

    def sendEndGameMessage(self, winningTeam, reason, extraData):
        messageType = GAME_MESSAGES_CONSTS.DRAW
        if winningTeam != 0:
            isWinner = avatar_getter.getPlayerTeam() == winningTeam
            if isWinner:
                messageType = GAME_MESSAGES_CONSTS.WIN
            else:
                messageType = GAME_MESSAGES_CONSTS.DEFEAT
        endGameMsgData = {'title': backport.text(R.strings.maps_training.finalBattleScreen.dyn(messageType)())}
        msg = PlayerMessageData(messageType, GAME_MESSAGES_CONSTS.DEFAULT_MESSAGE_LENGTH, GAME_MESSAGES_CONSTS.GAME_MESSAGE_PRIORITY_END_GAME, endGameMsgData)
        self._addMessage(msg.getDict())