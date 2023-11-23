# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/comp7_bonus_model.py
from enum import IntEnum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class DogTagType(IntEnum):
    ENGRAVING = 0
    BACKGROUND = 1


class Comp7BonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(Comp7BonusModel, self).__init__(properties=properties, commands=commands)

    def getDogTagType(self):
        return DogTagType(self._getNumber(8))

    def setDogTagType(self, value):
        self._setNumber(8, value.value)

    def getIsPeriodic(self):
        return self._getBool(9)

    def setIsPeriodic(self, value):
        self._setBool(9, value)

    def getOverlayType(self):
        return self._getString(10)

    def setOverlayType(self, value):
        self._setString(10, value)

    def _initialize(self):
        super(Comp7BonusModel, self)._initialize()
        self._addNumberProperty('dogTagType')
        self._addBoolProperty('isPeriodic', False)
        self._addStringProperty('overlayType', '')