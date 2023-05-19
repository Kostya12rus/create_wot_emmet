# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicBattleTrainingRoomMeta.py
from gui.Scaleform.daapi.view.lobby.trainings.TrainingRoomBase import TrainingRoomBase

class EpicBattleTrainingRoomMeta(TrainingRoomBase):

    def onChangeTeamLane(self, accID, team, lane):
        self._printOverrideError('onChangeTeamLane')

    def onSwapTeamLane(self, fromTeam, fromLane, toTeam, toLane):
        self._printOverrideError('onSwapTeamLane')