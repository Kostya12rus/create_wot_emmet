# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/components/ny_with_roman_numbers_model.py
from frameworks.wulf import ViewModel

class NyWithRomanNumbersModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NyWithRomanNumbersModel, self).__init__(properties=properties, commands=commands)

    def getIsRomanNumbersAllowed(self):
        return self._getBool(0)

    def setIsRomanNumbersAllowed(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(NyWithRomanNumbersModel, self)._initialize()
        self._addBoolProperty('isRomanNumbersAllowed', True)