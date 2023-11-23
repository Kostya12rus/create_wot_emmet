# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/stepper_view_model.py
from frameworks.wulf import ViewModel

class StepperViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(StepperViewModel, self).__init__(properties=properties, commands=commands)

    def getMinimum(self):
        return self._getNumber(0)

    def setMinimum(self, value):
        self._setNumber(0, value)

    def getMaximum(self):
        return self._getNumber(1)

    def setMaximum(self, value):
        self._setNumber(1, value)

    def getStepSize(self):
        return self._getNumber(2)

    def setStepSize(self, value):
        self._setNumber(2, value)

    def getValue(self):
        return self._getNumber(3)

    def setValue(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(StepperViewModel, self)._initialize()
        self._addNumberProperty('minimum', 0)
        self._addNumberProperty('maximum', 0)
        self._addNumberProperty('stepSize', 0)
        self._addNumberProperty('value', 0)