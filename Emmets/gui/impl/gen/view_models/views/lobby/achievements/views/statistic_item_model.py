# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/statistic_item_model.py
from frameworks.wulf import ViewModel

class StatisticItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(StatisticItemModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getMainValue(self):
        return self._getString(1)

    def setMainValue(self, value):
        self._setString(1, value)

    def getAdditionalValue(self):
        return self._getString(2)

    def setAdditionalValue(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(StatisticItemModel, self)._initialize()
        self._addStringProperty('type', 'battles')
        self._addStringProperty('mainValue', '')
        self._addStringProperty('additionalValue', '')