# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/vehicle_btn_model.py
from frameworks.wulf import ViewModel

class VehicleBtnModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehicleBtnModel, self).__init__(properties=properties, commands=commands)

    def getFlag(self):
        return self._getString(0)

    def setFlag(self, value):
        self._setString(0, value)

    def getVehType(self):
        return self._getString(1)

    def setVehType(self, value):
        self._setString(1, value)

    def getVehLvl(self):
        return self._getString(2)

    def setVehLvl(self, value):
        self._setString(2, value)

    def getVehIcon(self):
        return self._getString(3)

    def setVehIcon(self, value):
        self._setString(3, value)

    def getVehName(self):
        return self._getString(4)

    def setVehName(self, value):
        self._setString(4, value)

    def getVisible(self):
        return self._getBool(5)

    def setVisible(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(VehicleBtnModel, self)._initialize()
        self._addStringProperty('flag', '')
        self._addStringProperty('vehType', '')
        self._addStringProperty('vehLvl', '')
        self._addStringProperty('vehIcon', '')
        self._addStringProperty('vehName', '')
        self._addBoolProperty('visible', False)