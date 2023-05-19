# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/vehicle_params_category.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.vehicle_params_item import VehicleParamsItem

class VehicleParamsCategory(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(VehicleParamsCategory, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)

    @staticmethod
    def getItemsType():
        return VehicleParamsItem

    def _initialize(self):
        super(VehicleParamsCategory, self)._initialize()
        self._addStringProperty('title', '')
        self._addArrayProperty('items', Array())