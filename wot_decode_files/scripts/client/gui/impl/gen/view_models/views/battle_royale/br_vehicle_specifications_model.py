# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/br_vehicle_specifications_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BrVehicleSpecificationsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BrVehicleSpecificationsModel, self).__init__(properties=properties, commands=commands)

    def getSpecName(self):
        return self._getResource(0)

    def setSpecName(self, value):
        self._setResource(0, value)

    def getIconSource(self):
        return self._getResource(1)

    def setIconSource(self, value):
        self._setResource(1, value)

    def _initialize(self):
        super(BrVehicleSpecificationsModel, self)._initialize()
        self._addResourceProperty('specName', R.invalid())
        self._addResourceProperty('iconSource', R.invalid())