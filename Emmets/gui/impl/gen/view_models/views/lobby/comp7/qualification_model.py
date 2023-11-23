# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/qualification_model.py
from frameworks.wulf import ViewModel

class QualificationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(QualificationModel, self).__init__(properties=properties, commands=commands)

    def getIsActive(self):
        return self._getBool(0)

    def setIsActive(self, value):
        self._setBool(0, value)

    def getBattlesCount(self):
        return self._getNumber(1)

    def setBattlesCount(self, value):
        self._setNumber(1, value)

    def getMaxBattlesCount(self):
        return self._getNumber(2)

    def setMaxBattlesCount(self, value):
        self._setNumber(2, value)

    def getIsRatingCalculation(self):
        return self._getBool(3)

    def setIsRatingCalculation(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(QualificationModel, self)._initialize()
        self._addBoolProperty('isActive', False)
        self._addNumberProperty('battlesCount', 0)
        self._addNumberProperty('maxBattlesCount', 0)
        self._addBoolProperty('isRatingCalculation', False)