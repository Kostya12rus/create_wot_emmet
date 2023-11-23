# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tankmen_voiceover_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tankman_model import TankmanModel

class TankmenVoiceoverViewModel(ViewModel):
    __slots__ = ('showShop', 'close')

    def __init__(self, properties=1, commands=2):
        super(TankmenVoiceoverViewModel, self).__init__(properties=properties, commands=commands)

    def getTankmen(self):
        return self._getArray(0)

    def setTankmen(self, value):
        self._setArray(0, value)

    @staticmethod
    def getTankmenType():
        return TankmanModel

    def _initialize(self):
        super(TankmenVoiceoverViewModel, self)._initialize()
        self._addArrayProperty('tankmen', Array())
        self.showShop = self._addCommand('showShop')
        self.close = self._addCommand('close')