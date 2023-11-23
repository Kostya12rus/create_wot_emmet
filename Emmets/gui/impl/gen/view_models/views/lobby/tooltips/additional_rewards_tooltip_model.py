# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tooltips/additional_rewards_tooltip_model.py
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class AdditionalRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(AdditionalRewardsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getHeaderText(self):
        return self._getResource(0)

    def setHeaderText(self, value):
        self._setResource(0, value)

    def getHeaderCount(self):
        return self._getNumber(1)

    def setHeaderCount(self, value):
        self._setNumber(1, value)

    def getDescription(self):
        return self._getResource(2)

    def setDescription(self, value):
        self._setResource(2, value)

    def getDescriptionCount(self):
        return self._getNumber(3)

    def setDescriptionCount(self, value):
        self._setNumber(3, value)

    def getBonus(self):
        return self._getArray(4)

    def setBonus(self, value):
        self._setArray(4, value)

    @staticmethod
    def getBonusType():
        return BonusModel

    def _initialize(self):
        super(AdditionalRewardsTooltipModel, self)._initialize()
        self._addResourceProperty('headerText', R.invalid())
        self._addNumberProperty('headerCount', 0)
        self._addResourceProperty('description', R.invalid())
        self._addNumberProperty('descriptionCount', 0)
        self._addArrayProperty('bonus', Array())