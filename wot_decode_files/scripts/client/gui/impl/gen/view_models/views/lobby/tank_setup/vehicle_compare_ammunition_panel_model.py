# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/vehicle_compare_ammunition_panel_model.py
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel

class VehicleCompareAmmunitionPanelModel(AmmunitionPanelViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=6, commands=3):
        super(VehicleCompareAmmunitionPanelModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(VehicleCompareAmmunitionPanelModel, self)._initialize()
        self.onClose = self._addCommand('onClose')