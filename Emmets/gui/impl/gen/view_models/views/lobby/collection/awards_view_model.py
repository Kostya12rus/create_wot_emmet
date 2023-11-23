# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/collection/awards_view_model.py
from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.collection.reward_model import RewardModel

class CollectionAwardState(Enum):
    COMPLETED = 'completed'
    ACTIVE = 'active'


class AwardsViewModel(ViewModel):
    __slots__ = ('onOpenCollection', 'onCloseCollection')

    def __init__(self, properties=5, commands=2):
        super(AwardsViewModel, self).__init__(properties=properties, commands=commands)

    def getCollectionName(self):
        return self._getString(0)

    def setCollectionName(self, value):
        self._setString(0, value)

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)

    def getBackground(self):
        return self._getString(2)

    def setBackground(self, value):
        self._setString(2, value)

    def getState(self):
        return CollectionAwardState(self._getString(3))

    def setState(self, value):
        self._setString(3, value.value)

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)

    @staticmethod
    def getRewardsType():
        return RewardModel

    def _initialize(self):
        super(AwardsViewModel, self)._initialize()
        self._addStringProperty('collectionName', '')
        self._addBoolProperty('isDisabled', False)
        self._addStringProperty('background', '')
        self._addStringProperty('state')
        self._addArrayProperty('rewards', Array())
        self.onOpenCollection = self._addCommand('onOpenCollection')
        self.onCloseCollection = self._addCommand('onCloseCollection')