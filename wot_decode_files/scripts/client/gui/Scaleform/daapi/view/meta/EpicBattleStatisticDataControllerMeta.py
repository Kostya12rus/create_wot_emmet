# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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