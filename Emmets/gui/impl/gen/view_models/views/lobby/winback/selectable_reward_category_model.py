# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/selectable_reward_category_model.py
from frameworks.wulf import ViewModel

class SelectableRewardCategoryModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SelectableRewardCategoryModel, self).__init__(properties=properties, commands=commands)

    def getIsDiscount(self):
        return self._getBool(0)

    def setIsDiscount(self, value):
        self._setBool(0, value)

    def getIsSelected(self):
        return self._getBool(1)

    def setIsSelected(self, value):
        self._setBool(1, value)

    def getIsCompensation(self):
        return self._getBool(2)

    def setIsCompensation(self, value):
        self._setBool(2, value)

    def getVehicleLevel(self):
        return self._getNumber(3)

    def setVehicleLevel(self, value):
        self._setNumber(3, value)

    def getRewardsSelected(self):
        return self._getNumber(4)

    def setRewardsSelected(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(SelectableRewardCategoryModel, self)._initialize()
        self._addBoolProperty('isDiscount', False)
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isCompensation', False)
        self._addNumberProperty('vehicleLevel', 0)
        self._addNumberProperty('rewardsSelected', 0)