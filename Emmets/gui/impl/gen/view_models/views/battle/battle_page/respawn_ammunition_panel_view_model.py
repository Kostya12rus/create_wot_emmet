# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/respawn_ammunition_panel_view_model.py
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel

class RespawnAmmunitionPanelViewModel(AmmunitionPanelViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=2):
        super(RespawnAmmunitionPanelViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(6)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def _initialize(self):
        super(RespawnAmmunitionPanelViewModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())