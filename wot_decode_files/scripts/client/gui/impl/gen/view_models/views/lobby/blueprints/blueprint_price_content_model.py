# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_price_content_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_value_price import BlueprintValuePrice

class BlueprintPriceContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BlueprintPriceContentModel, self).__init__(properties=properties, commands=commands)

    @property
    def valueMain(self):
        return self._getViewModel(0)

    @staticmethod
    def getValueMainType():
        return BlueprintValuePrice

    @property
    def additionalValues(self):
        return self._getViewModel(1)

    @staticmethod
    def getAdditionalValuesType():
        return ListModel

    def getTooltipId(self):
        return self._getNumber(2)

    def setTooltipId(self, value):
        self._setNumber(2, value)

    def getHasAdditionalCost(self):
        return self._getBool(3)

    def setHasAdditionalCost(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(BlueprintPriceContentModel, self)._initialize()
        self._addViewModelProperty('valueMain', BlueprintValuePrice())
        self._addViewModelProperty('additionalValues', ListModel())
        self._addNumberProperty('tooltipId', 0)
        self._addBoolProperty('hasAdditionalCost', False)