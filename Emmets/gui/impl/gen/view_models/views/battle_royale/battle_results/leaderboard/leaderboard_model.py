# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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