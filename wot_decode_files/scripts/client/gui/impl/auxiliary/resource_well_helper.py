# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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