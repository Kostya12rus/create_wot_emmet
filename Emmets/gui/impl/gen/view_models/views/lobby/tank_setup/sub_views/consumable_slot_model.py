# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/consumable_slot_model.py
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel

class ConsumableSlotModel(BaseSlotModel):
    __slots__ = ()

    def __init__(self, properties=24, commands=0):
        super(ConsumableSlotModel, self).__init__(properties=properties, commands=commands)

    def getDescription(self):
        return self._getString(20)

    def setDescription(self, value):
        self._setString(20, value)

    def getIsBuiltIn(self):
        return self._getBool(21)

    def setIsBuiltIn(self, value):
        self._setBool(21, value)

    def getItemName(self):
        return self._getString(22)

    def setItemName(self, value):
        self._setString(22, value)

    def getIsBuyMoreDisabled(self):
        return self._getBool(23)

    def setIsBuyMoreDisabled(self, value):
        self._setBool(23, value)

    def _initialize(self):
        super(ConsumableSlotModel, self)._initialize()
        self._addStringProperty('description', '')
        self._addBoolProperty('isBuiltIn', False)
        self._addStringProperty('itemName', '')
        self._addBoolProperty('isBuyMoreDisabled', False)