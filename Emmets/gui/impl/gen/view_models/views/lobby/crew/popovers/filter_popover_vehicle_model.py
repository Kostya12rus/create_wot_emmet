# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/popovers/filter_popover_vehicle_model.py
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class FilterPopoverVehicleModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(FilterPopoverVehicleModel, self).__init__(properties=properties, commands=commands)

    def getIsSelected(self):
        return self._getBool(9)

    def setIsSelected(self, value):
        self._setBool(9, value)

    def _initialize(self):
        super(FilterPopoverVehicleModel, self)._initialize()
        self._addBoolProperty('isSelected', False)