# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/battle_boosters_setup_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.battle_booster_slot_model import BattleBoosterSlotModel

class BattleBoostersSetupModel(BaseSetupModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=7):
        super(BattleBoostersSetupModel, self).__init__(properties=properties, commands=commands)

    def getSlots(self):
        return self._getArray(5)

    def setSlots(self, value):
        self._setArray(5, value)

    @staticmethod
    def getSlotsType():
        return BattleBoosterSlotModel

    def _initialize(self):
        super(BattleBoostersSetupModel, self)._initialize()
        self._addArrayProperty('slots', Array())