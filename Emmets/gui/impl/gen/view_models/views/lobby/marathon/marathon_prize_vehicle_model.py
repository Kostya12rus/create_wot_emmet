# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/marathon/marathon_prize_vehicle_model.py
from frameworks.wulf import ViewModel

class MarathonPrizeVehicleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MarathonPrizeVehicleModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(MarathonPrizeVehicleModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('type', '')
        self._addNumberProperty('level', 0)