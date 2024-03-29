# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/nation_change/nation_change_device_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NationChangeDeviceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(NationChangeDeviceModel, self).__init__(properties=properties, commands=commands)

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)

    def getIsImproved(self):
        return self._getBool(1)

    def setIsImproved(self, value):
        self._setBool(1, value)

    def getIsTrophyBasic(self):
        return self._getBool(2)

    def setIsTrophyBasic(self, value):
        self._setBool(2, value)

    def getIsTrophyUpgraded(self):
        return self._getBool(3)

    def setIsTrophyUpgraded(self, value):
        self._setBool(3, value)

    def getIsModernized(self):
        return self._getBool(4)

    def setIsModernized(self, value):
        self._setBool(4, value)

    def getLevel(self):
        return self._getNumber(5)

    def setLevel(self, value):
        self._setNumber(5, value)

    def getIntCD(self):
        return self._getNumber(6)

    def setIntCD(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(NationChangeDeviceModel, self)._initialize()
        self._addResourceProperty('image', R.invalid())
        self._addBoolProperty('isImproved', False)
        self._addBoolProperty('isTrophyBasic', False)
        self._addBoolProperty('isTrophyUpgraded', False)
        self._addBoolProperty('isModernized', False)
        self._addNumberProperty('level', 1)
        self._addNumberProperty('intCD', 0)