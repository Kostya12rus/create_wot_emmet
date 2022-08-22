# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/auxiliary/resource_well_helper.py
import typing
from helpers import dependency
from skeletons.gui.game_control import IResourceWellController
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.resource_well.vehicle_counter_model import VehicleCounterModel

@dependency.replace_none_kwargs(resourceWell=IResourceWellController)
def fillVehicleCounter(vehicleCounterModel, resourceWell=None):
    topRewardsCount = resourceWell.getRewardLeftCount(isTop=True)
    isTopReward = bool(topRewardsCount)
    if isTopReward:
        vehicleCounterModel.setVehicleCount(topRewardsCount)
    else:
        vehicleCounterModel.setVehicleCount(resourceWell.getRewardLeftCount(isTop=False))
    vehicleCounterModel.setIsTopVehicle(isTopReward)
    vehicleCounterModel.setIsVehicleCountAvailable(resourceWell.isRewardCountAvailable(isTopReward))