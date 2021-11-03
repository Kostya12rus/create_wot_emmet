# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicBattleTrainingRoomMeta.py
from gui.Scaleform.daapi.view.lobby.trainings.TrainingRoomBase import TrainingRoomBase

class EpicBattleTrainingRoomMeta(TrainingRoomBase):

    def onChangeTeamLane(self, accID, team, lane):
        self._printOverrideError('onChangeTeamLane')

    def onSwapTeamLane(self, fromTeam, fromLane, toTeam, toLane):
        self._printOverrideError('onSwapTeamLane')