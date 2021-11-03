# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_configurator_ammo_inject.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants
from gui.impl.lobby.vehicle_compare.ammunition_panel import CompareAmmunitionPanelView

class VehicleCompareConfiguratorAmmoInject(InjectComponentAdaptor):

    def update(self):
        self.getInjectView().update()

    def updateShells(self):
        self.getInjectView().updateSection(TankSetupConstants.TOGGLE_SHELLS)

    def updateCamouflage(self):
        self.getInjectView().updateSection(TankSetupConstants.TOGGLE_CAMOUFLAGE)

    def _makeInjectView(self):
        ammunitionPanel = CompareAmmunitionPanelView()
        return ammunitionPanel