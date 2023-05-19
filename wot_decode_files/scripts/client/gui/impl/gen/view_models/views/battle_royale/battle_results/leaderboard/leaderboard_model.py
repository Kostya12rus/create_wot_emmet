# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/leaderboard/leaderboard_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.leaderboard.group_model import GroupModel

class LeaderboardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LeaderboardModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getGroupList(self):
        return self._getArray(1)

    def setGroupList(self, value):
        self._setArray(1, value)

    @staticmethod
    def getGroupListType():
        return GroupModel

    def _initialize(self):
        super(LeaderboardModel, self)._initialize()
        self._addStringProperty('type', 'solo')
        self._addArrayProperty('groupList', Array())