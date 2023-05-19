# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/counter_model.py
from frameworks.wulf import ViewModel

class CounterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(CounterModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(CounterModel, self)._initialize()
        self._addNumberProperty('value', -1)