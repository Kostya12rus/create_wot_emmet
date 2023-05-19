# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic/battle_loading.py
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class EpicBattleLoading(BattleLoading):
    lobbyContext = dependency.descriptor(ILobbyContext)

    def _getBattlesCount(self):
        return self.lobbyContext.getEpicBattlesCount()