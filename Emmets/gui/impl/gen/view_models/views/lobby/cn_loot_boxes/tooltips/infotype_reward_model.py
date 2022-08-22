# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/cn_loot_boxes/tooltips/infotype_reward_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class InfotypeRewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(InfotypeRewardModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)

    def _initialize(self):
        super(InfotypeRewardModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addNumberProperty('count', 0)
        self._addResourceProperty('icon', R.invalid())