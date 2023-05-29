# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_view_veh_params.py
from gui.Scaleform.daapi.view.lobby.hangar.VehicleParameters import VehicleParameters, TankSetupParamsDataProvider
from gui.Scaleform.daapi.view.lobby.tank_setup.ammunition_setup_vehicle import g_tankSetupVehicle
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS

class AmmunitionSetupViewVehicleParams(VehicleParameters):

    def _createDataProvider(self):
        return TankSetupParamsDataProvider(TOOLTIPS_CONSTANTS.VEHICLE_TANK_SETUP_PARAMETERS)

    def _getVehicleCache(self):
        return g_tankSetupVehicle