# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/ranked/stats_exchange.py
from gui.Scaleform.daapi.view.battle.classic.stats_exchange import ClassicStatisticsDataController, DynamicVehicleStatsComponent
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import createExchangeBroker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import vehicle
from gui.battle_control.arena_info import vos_collections
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController

class RankedVehicleInfoComponent(vehicle.VehicleInfoComponent):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def addVehicleInfo(self, vInfoVO, overrides):
        super(RankedVehicleInfoComponent, self).addVehicleInfo(vInfoVO, overrides)
        displayInfo = self.__rankedController.getRankDisplayInfoForBattle(vInfoVO.ranked.rank)
        return self._data.update({'level': displayInfo.level, 
           'division': displayInfo.division, 
           'isGroup': displayInfo.isGroup})


class RankedStatisticsDataController(ClassicStatisticsDataController):

    def _createExchangeBroker(self, exchangeCtx):
        exchangeBroker = createExchangeBroker(exchangeCtx)
        exchangeBroker.setVehiclesInfoExchange(vehicle.VehiclesExchangeBlock(RankedVehicleInfoComponent(), positionComposer=broker.BiDirectionComposer(), idsComposers=(
         vehicle.TeamsSortedIDsComposer(sortKey=vos_collections.RankSortKey),
         vehicle.TeamsCorrelationIDsComposer()), statsComposers=None))
        exchangeBroker.setVehiclesStatsExchange(vehicle.VehiclesExchangeBlock(DynamicVehicleStatsComponent(), positionComposer=broker.BiDirectionComposer(), idsComposers=None, statsComposers=(
         vehicle.TotalStatsComposer(),)))
        exchangeBroker.setVehicleStatusExchange(vehicle.VehicleStatusComponent(idsComposers=(
         vehicle.TeamsSortedIDsComposer(sortKey=vos_collections.RankSortKey),
         vehicle.TeamsCorrelationIDsComposer()), statsComposers=(
         vehicle.TotalStatsComposer(),)))
        return exchangeBroker