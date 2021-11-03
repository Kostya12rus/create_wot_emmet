# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/br_base_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.leaderboard.leaderboard_model import LeaderboardModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.player_vehicle_status_model import PlayerVehicleStatusModel

class BrBaseViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BrBaseViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def leaderboardModel(self):
        return self._getViewModel(0)

    @property
    def playerVehicleStatus(self):
        return self._getViewModel(1)

    def _initialize(self):
        super(BrBaseViewModel, self)._initialize()
        self._addViewModelProperty('leaderboardModel', LeaderboardModel())
        self._addViewModelProperty('playerVehicleStatus', PlayerVehicleStatusModel())