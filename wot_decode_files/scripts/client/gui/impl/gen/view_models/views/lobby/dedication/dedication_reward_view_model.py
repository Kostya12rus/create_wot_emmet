# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dedication/dedication_reward_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class DedicationRewardViewModel(ViewModel):
    __slots__ = ()
    BATTLES_150K = '150'
    BATTLES_200K = '200'
    BATTLES_250K = '250'
    BATTLES_300K = '300'

    def __init__(self, properties=2, commands=0):
        super(DedicationRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getMainRewards(self):
        return self._getArray(0)

    def setMainRewards(self, value):
        self._setArray(0, value)

    def getLevel(self):
        return self._getString(1)

    def setLevel(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(DedicationRewardViewModel, self)._initialize()
        self._addArrayProperty('mainRewards', Array())
        self._addStringProperty('level', '')