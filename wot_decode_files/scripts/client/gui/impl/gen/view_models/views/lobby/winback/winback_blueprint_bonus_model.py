# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/winback_blueprint_bonus_model.py
from gui.impl.gen.view_models.common.missions.bonuses.blueprint_bonus_model import BlueprintBonusModel

class WinbackBlueprintBonusModel(BlueprintBonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(WinbackBlueprintBonusModel, self).__init__(properties=properties, commands=commands)

    def getAmountInStorage(self):
        return self._getNumber(9)

    def setAmountInStorage(self, value):
        self._setNumber(9, value)

    def getIsSelected(self):
        return self._getBool(10)

    def setIsSelected(self, value):
        self._setBool(10, value)

    def _initialize(self):
        super(WinbackBlueprintBonusModel, self)._initialize()
        self._addNumberProperty('amountInStorage', 0)
        self._addBoolProperty('isSelected', False)