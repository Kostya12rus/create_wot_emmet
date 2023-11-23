# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/quick_training_discount_tooltip_model.py
from frameworks.wulf import ViewModel

class QuickTrainingDiscountTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(QuickTrainingDiscountTooltipModel, self).__init__(properties=properties, commands=commands)

    def getOldFreeXpBaseValue(self):
        return self._getNumber(0)

    def setOldFreeXpBaseValue(self, value):
        self._setNumber(0, value)

    def getNewFreeXpBaseValue(self):
        return self._getNumber(1)

    def setNewFreeXpBaseValue(self, value):
        self._setNumber(1, value)

    def getOldXpExchangeValue(self):
        return self._getNumber(2)

    def setOldXpExchangeValue(self, value):
        self._setNumber(2, value)

    def getNewXpExchangeValue(self):
        return self._getNumber(3)

    def setNewXpExchangeValue(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(QuickTrainingDiscountTooltipModel, self)._initialize()
        self._addNumberProperty('oldFreeXpBaseValue', 1)
        self._addNumberProperty('newFreeXpBaseValue', 1)
        self._addNumberProperty('oldXpExchangeValue', 1)
        self._addNumberProperty('newXpExchangeValue', 1)