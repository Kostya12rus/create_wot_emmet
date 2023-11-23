# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/tooltips/deconstruct_from_inventory_tooltip_model.py
from frameworks.wulf import ViewModel

class DeconstructFromInventoryTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DeconstructFromInventoryTooltipModel, self).__init__(properties=properties, commands=commands)

    def getEquipmentName(self):
        return self._getString(0)

    def setEquipmentName(self, value):
        self._setString(0, value)

    def getEquipmentAmount(self):
        return self._getNumber(1)

    def setEquipmentAmount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(DeconstructFromInventoryTooltipModel, self)._initialize()
        self._addStringProperty('equipmentName', '')
        self._addNumberProperty('equipmentAmount', 0)