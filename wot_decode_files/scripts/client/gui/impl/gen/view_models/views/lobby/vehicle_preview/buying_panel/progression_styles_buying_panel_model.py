# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_preview/buying_panel/progression_styles_buying_panel_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class SwitcherType(IntEnum):
    DIGITAL = 0
    TEXT = 1


class ProgressionStylesBuyingPanelModel(ViewModel):
    __slots__ = ('onChange', )

    def __init__(self, properties=7, commands=1):
        super(ProgressionStylesBuyingPanelModel, self).__init__(properties=properties, commands=commands)

    def getCurrentLevel(self):
        return self._getNumber(0)

    def setCurrentLevel(self, value):
        self._setNumber(0, value)

    def getSelectedLevel(self):
        return self._getNumber(1)

    def setSelectedLevel(self, value):
        self._setNumber(1, value)

    def getIsReady(self):
        return self._getBool(2)

    def setIsReady(self, value):
        self._setBool(2, value)

    def getNumberOfBullets(self):
        return self._getNumber(3)

    def setNumberOfBullets(self, value):
        self._setNumber(3, value)

    def getIsBulletsBeforeCurrentDisabled(self):
        return self._getBool(4)

    def setIsBulletsBeforeCurrentDisabled(self, value):
        self._setBool(4, value)

    def getSwitcherType(self):
        return SwitcherType(self._getNumber(5))

    def setSwitcherType(self, value):
        self._setNumber(5, value.value)

    def getStyleID(self):
        return self._getNumber(6)

    def setStyleID(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(ProgressionStylesBuyingPanelModel, self)._initialize()
        self._addNumberProperty('currentLevel', 0)
        self._addNumberProperty('selectedLevel', 0)
        self._addBoolProperty('isReady', False)
        self._addNumberProperty('numberOfBullets', 4)
        self._addBoolProperty('isBulletsBeforeCurrentDisabled', True)
        self._addNumberProperty('switcherType')
        self._addNumberProperty('styleID', 0)
        self.onChange = self._addCommand('onChange')