# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_exchange_rewards_model.py
from frameworks.wulf import ViewModel

class BattleMattersExchangeRewardsModel(ViewModel):
    __slots__ = ('onConfirm', 'onClose')

    def __init__(self, properties=2, commands=2):
        super(BattleMattersExchangeRewardsModel, self).__init__(properties=properties, commands=commands)

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)

    def getVehicleUserName(self):
        return self._getString(1)

    def setVehicleUserName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(BattleMattersExchangeRewardsModel, self)._initialize()
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('vehicleUserName', '')
        self.onConfirm = self._addCommand('onConfirm')
        self.onClose = self._addCommand('onClose')