# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/vehicle_compare_ammunition_panel_model.py
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel

class VehicleCompareAmmunitionPanelModel(AmmunitionPanelViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=7, commands=3):
        super(VehicleCompareAmmunitionPanelModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(VehicleCompareAmmunitionPanelModel, self)._initialize()
        self.onClose = self._addCommand('onClose')