# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_reserves/disabled_category.py
from enum import Enum
from frameworks.wulf import ViewModel

class CategoryType(Enum):
    PERSONAL = 'personal'
    CLAN = 'clan'
    EVENT = 'event'


class DisabledCategory(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DisabledCategory, self).__init__(properties=properties, commands=commands)

    def getCategoryType(self):
        return CategoryType(self._getString(0))

    def setCategoryType(self, value):
        self._setString(0, value.value)

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(DisabledCategory, self)._initialize()
        self._addStringProperty('categoryType')
        self._addBoolProperty('isDisabled', False)