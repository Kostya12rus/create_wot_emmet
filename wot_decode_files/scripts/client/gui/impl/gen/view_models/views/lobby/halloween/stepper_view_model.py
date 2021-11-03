# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/stepper_view_model.py
from frameworks.wulf import ViewModel

class StepperViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(StepperViewModel, self).__init__(properties=properties, commands=commands)

    def getMaximumValue(self):
        return self._getNumber(0)

    def setMaximumValue(self, value):
        self._setNumber(0, value)

    def getSelectedValue(self):
        return self._getNumber(1)

    def setSelectedValue(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(StepperViewModel, self)._initialize()
        self._addNumberProperty('maximumValue', 0)
        self._addNumberProperty('selectedValue', 0)