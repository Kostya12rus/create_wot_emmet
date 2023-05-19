# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/battle_booster_slot_model.py
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel

class BattleBoosterSlotModel(BaseSlotModel):
    __slots__ = ()

    def __init__(self, properties=23, commands=0):
        super(BattleBoosterSlotModel, self).__init__(properties=properties, commands=commands)

    def getDescription(self):
        return self._getString(20)

    def setDescription(self, value):
        self._setString(20, value)

    def getIsBuyMoreVisible(self):
        return self._getBool(21)

    def setIsBuyMoreVisible(self, value):
        self._setBool(21, value)

    def getIsBuyMoreDisabled(self):
        return self._getBool(22)

    def setIsBuyMoreDisabled(self, value):
        self._setBool(22, value)

    def _initialize(self):
        super(BattleBoosterSlotModel, self)._initialize()
        self._addStringProperty('description', '')
        self._addBoolProperty('isBuyMoreVisible', True)
        self._addBoolProperty('isBuyMoreDisabled', False)