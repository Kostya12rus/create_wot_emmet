# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/daily_experience_base_model.py
from frameworks.wulf import ViewModel

class DailyExperienceBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DailyExperienceBaseModel, self).__init__(properties=properties, commands=commands)

    def getIsTankPremiumActive(self):
        return self._getBool(0)

    def setIsTankPremiumActive(self, value):
        self._setBool(0, value)

    def getMultiplier(self):
        return self._getNumber(1)

    def setMultiplier(self, value):
        self._setNumber(1, value)

    def getLeftBonusCount(self):
        return self._getNumber(2)

    def setLeftBonusCount(self, value):
        self._setNumber(2, value)

    def getTotalBonusCount(self):
        return self._getNumber(3)

    def setTotalBonusCount(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(DailyExperienceBaseModel, self)._initialize()
        self._addBoolProperty('isTankPremiumActive', False)
        self._addNumberProperty('multiplier', 1)
        self._addNumberProperty('leftBonusCount', 0)
        self._addNumberProperty('totalBonusCount', 5)