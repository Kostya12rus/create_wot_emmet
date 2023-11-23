# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/details_device_model.py
from frameworks.wulf import ViewModel

class DetailsDeviceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(DetailsDeviceModel, self).__init__(properties=properties, commands=commands)

    def getOverlayType(self):
        return self._getString(0)

    def setOverlayType(self, value):
        self._setString(0, value)

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)

    def getDeviceName(self):
        return self._getString(2)

    def setDeviceName(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(DetailsDeviceModel, self)._initialize()
        self._addStringProperty('overlayType', '')
        self._addNumberProperty('level', 0)
        self._addStringProperty('deviceName', '')