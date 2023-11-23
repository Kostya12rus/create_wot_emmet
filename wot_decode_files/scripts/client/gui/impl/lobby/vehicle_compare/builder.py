# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_compare/builder.py
from gui.impl.gen.view_models.views.lobby.tank_setup.main_tank_setup_model import MainTankSetupModel
from gui.impl.lobby.vehicle_compare.battle_booster import CompareBattleBoosterSetupSubView
from gui.impl.lobby.vehicle_compare.consumable import CompareConsumableSetupSubView
from gui.impl.lobby.vehicle_compare.interactors import CompareConsumableInteractor, CompareOptDeviceInteractor, CompareBattleBoosterInteractor
from gui.impl.lobby.vehicle_compare.opt_device import CompareOptDeviceSetupSubView
from gui.impl.lobby.tank_setup.tank_setup_builder import TankSetupBuilder

class CompareTankSetupBuilder(TankSetupBuilder):
    __slots__ = ()

    def __init__(self, vehItem):
        super(CompareTankSetupBuilder, self).__init__(MainTankSetupModel, vehItem)

    def configureComponents(self, viewModel):
        components = super(CompareTankSetupBuilder, self).configureComponents(viewModel)
        self.addComponent(components, viewModel.consumablesSetup, CompareConsumableSetupSubView, CompareConsumableInteractor(self._vehItem))
        self.addComponent(components, viewModel.optDevicesSetup, CompareOptDeviceSetupSubView, CompareOptDeviceInteractor(self._vehItem))
        self.addComponent(components, viewModel.battleBoostersSetup, CompareBattleBoosterSetupSubView, CompareBattleBoosterInteractor(self._vehItem))
        return components