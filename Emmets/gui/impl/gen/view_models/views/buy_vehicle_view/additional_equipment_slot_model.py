# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/buy_vehicle_view/additional_equipment_slot_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class AdditionalEquipmentSlotModel(ViewModel):
    __slots__ = ('onSelectedChange', )

    def __init__(self, properties=4, commands=1):
        super(AdditionalEquipmentSlotModel, self).__init__(properties=properties, commands=commands)

    @property
    def actionPrices(self):
        return self._getViewModel(0)

    @staticmethod
    def getActionPricesType():
        return ListModel

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)

    def getIsDisabledTooltip(self):
        return self._getBool(3)

    def setIsDisabledTooltip(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(AdditionalEquipmentSlotModel, self)._initialize()
        self._addViewModelProperty('actionPrices', ListModel())
        self._addBoolProperty('isEnabled', False)
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isDisabledTooltip', False)
        self.onSelectedChange = self._addCommand('onSelectedChange')