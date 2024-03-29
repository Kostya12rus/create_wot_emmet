# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/squad_bonus_item_renderer_model.py
from frameworks.wulf import ViewModel

class SquadBonusItemRendererModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SquadBonusItemRendererModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getString(0)

    def setLevel(self, value):
        self._setString(0, value)

    def getDefeatValue(self):
        return self._getNumber(1)

    def setDefeatValue(self, value):
        self._setNumber(1, value)

    def getWinValue(self):
        return self._getNumber(2)

    def setWinValue(self, value):
        self._setNumber(2, value)

    def getIsCurrentLevel(self):
        return self._getBool(3)

    def setIsCurrentLevel(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(SquadBonusItemRendererModel, self)._initialize()
        self._addStringProperty('level', '')
        self._addNumberProperty('defeatValue', 0)
        self._addNumberProperty('winValue', 0)
        self._addBoolProperty('isCurrentLevel', False)