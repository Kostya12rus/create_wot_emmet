# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_main_reward_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_vehicle_model import BattleMattersVehicleModel

class BattleMattersMainRewardViewModel(ViewModel):
    __slots__ = ('onShowView', 'onStart', 'onPreview', 'onBack', 'onClose')

    def __init__(self, properties=2, commands=5):
        super(BattleMattersMainRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getIsWelcomeScreen(self):
        return self._getBool(0)

    def setIsWelcomeScreen(self, value):
        self._setBool(0, value)

    def getVehicles(self):
        return self._getArray(1)

    def setVehicles(self, value):
        self._setArray(1, value)

    @staticmethod
    def getVehiclesType():
        return BattleMattersVehicleModel

    def _initialize(self):
        super(BattleMattersMainRewardViewModel, self)._initialize()
        self._addBoolProperty('isWelcomeScreen', False)
        self._addArrayProperty('vehicles', Array())
        self.onShowView = self._addCommand('onShowView')
        self.onStart = self._addCommand('onStart')
        self.onPreview = self._addCommand('onPreview')
        self.onBack = self._addCommand('onBack')
        self.onClose = self._addCommand('onClose')