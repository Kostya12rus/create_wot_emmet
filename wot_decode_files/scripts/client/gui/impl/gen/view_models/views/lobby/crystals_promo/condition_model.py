# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crystals_promo/condition_model.py
from frameworks.wulf import ViewModel

class ConditionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ConditionModel, self).__init__(properties=properties, commands=commands)

    def getPosition(self):
        return self._getNumber(0)

    def setPosition(self, value):
        self._setNumber(0, value)

    def getForWin(self):
        return self._getNumber(1)

    def setForWin(self, value):
        self._setNumber(1, value)

    def getForDefeat(self):
        return self._getNumber(2)

    def setForDefeat(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(ConditionModel, self)._initialize()
        self._addNumberProperty('position', 0)
        self._addNumberProperty('forWin', 0)
        self._addNumberProperty('forDefeat', 0)