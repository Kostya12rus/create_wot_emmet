# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/tooltips/ny_loot_box_statistics_customization_model.py
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_vehicle_renderer_model import NyVehicleRendererModel

class NyLootBoxStatisticsCustomizationModel(NyVehicleRendererModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NyLootBoxStatisticsCustomizationModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(3)

    def setName(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(NyLootBoxStatisticsCustomizationModel, self)._initialize()
        self._addStringProperty('name', '')