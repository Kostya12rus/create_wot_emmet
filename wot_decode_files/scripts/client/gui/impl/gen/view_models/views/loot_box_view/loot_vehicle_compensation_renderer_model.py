# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/loot_vehicle_compensation_renderer_model.py
from gui.impl.gen.view_models.views.loot_box_view.loot_compensation_renderer_model import LootCompensationRendererModel

class LootVehicleCompensationRendererModel(LootCompensationRendererModel):
    __slots__ = ()

    def __init__(self, properties=29, commands=0):
        super(LootVehicleCompensationRendererModel, self).__init__(properties=properties, commands=commands)

    def getVehicleName(self):
        return self._getString(25)

    def setVehicleName(self, value):
        self._setString(25, value)

    def getVehicleType(self):
        return self._getString(26)

    def setVehicleType(self, value):
        self._setString(26, value)

    def getVehicleLvl(self):
        return self._getString(27)

    def setVehicleLvl(self, value):
        self._setString(27, value)

    def getIsElite(self):
        return self._getBool(28)

    def setIsElite(self, value):
        self._setBool(28, value)

    def _initialize(self):
        super(LootVehicleCompensationRendererModel, self)._initialize()
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('vehicleType', '')
        self._addStringProperty('vehicleLvl', '')
        self._addBoolProperty('isElite', True)