# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_rank_model.py
from frameworks.wulf import ViewModel

class ModeSelectorRankModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ModeSelectorRankModel, self).__init__(properties=properties, commands=commands)

    def getDivisionID(self):
        return self._getNumber(0)

    def setDivisionID(self, value):
        self._setNumber(0, value)

    def getRankID(self):
        return self._getNumber(1)

    def setRankID(self, value):
        self._setNumber(1, value)

    def getRankName(self):
        return self._getNumber(2)

    def setRankName(self, value):
        self._setNumber(2, value)

    def getIsQualification(self):
        return self._getBool(3)

    def setIsQualification(self, value):
        self._setBool(3, value)

    def getIsUnburnable(self):
        return self._getBool(4)

    def setIsUnburnable(self, value):
        self._setBool(4, value)

    def getShieldHP(self):
        return self._getNumber(5)

    def setShieldHP(self, value):
        self._setNumber(5, value)

    def _initialize(self):
        super(ModeSelectorRankModel, self)._initialize()
        self._addNumberProperty('divisionID', 0)
        self._addNumberProperty('rankID', 0)
        self._addNumberProperty('rankName', 0)
        self._addBoolProperty('isQualification', False)
        self._addBoolProperty('isUnburnable', False)
        self._addNumberProperty('shieldHP', 0)