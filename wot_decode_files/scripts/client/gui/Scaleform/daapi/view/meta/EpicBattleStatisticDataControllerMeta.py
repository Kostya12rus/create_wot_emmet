# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicBattleStatisticDataControllerMeta.py
from gui.Scaleform.daapi.view.battle.shared.stats_exchange.stats_ctrl import BattleStatisticsDataController

class EpicBattleStatisticDataControllerMeta(BattleStatisticsDataController):

    def as_updateEpicPlayerStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEpicPlayerStats(data)

    def as_setEpicVehiclesStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setEpicVehiclesStats(data)

    def as_updateEpicVehiclesStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEpicVehiclesStats(data)