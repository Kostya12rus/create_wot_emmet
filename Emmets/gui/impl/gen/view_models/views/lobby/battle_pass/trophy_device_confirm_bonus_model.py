# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/trophy_device_confirm_bonus_model.py
from frameworks.wulf import ViewModel

class TrophyDeviceConfirmBonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TrophyDeviceConfirmBonusModel, self).__init__(properties=properties, commands=commands)

    def getKpiName(self):
        return self._getString(0)

    def setKpiName(self, value):
        self._setString(0, value)

    def getBaseValue(self):
        return self._getString(1)

    def setBaseValue(self, value):
        self._setString(1, value)

    def getUpgradedValue(self):
        return self._getString(2)

    def setUpgradedValue(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(TrophyDeviceConfirmBonusModel, self)._initialize()
        self._addStringProperty('kpiName', '')
        self._addStringProperty('baseValue', '')
        self._addStringProperty('upgradedValue', '')