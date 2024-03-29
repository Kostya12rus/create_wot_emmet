# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/ranked/year_leaderboard_view_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class YearLeaderboardViewModel(ViewModel):
    __slots__ = ('onLeaderboardBtnClick', )

    def __init__(self, properties=6, commands=1):
        super(YearLeaderboardViewModel, self).__init__(properties=properties, commands=commands)

    def getPlayerName(self):
        return self._getString(0)

    def setPlayerName(self, value):
        self._setString(0, value)

    def getPlayerClan(self):
        return self._getString(1)

    def setPlayerClan(self, value):
        self._setString(1, value)

    def getPositionsTotal(self):
        return self._getNumber(2)

    def setPositionsTotal(self, value):
        self._setNumber(2, value)

    def getPosition(self):
        return self._getNumber(3)

    def setPosition(self, value):
        self._setNumber(3, value)

    def getRewardId(self):
        return self._getNumber(4)

    def setRewardId(self, value):
        self._setNumber(4, value)

    def getBgImage(self):
        return self._getResource(5)

    def setBgImage(self, value):
        self._setResource(5, value)

    def _initialize(self):
        super(YearLeaderboardViewModel, self)._initialize()
        self._addStringProperty('playerName', '')
        self._addStringProperty('playerClan', '')
        self._addNumberProperty('positionsTotal', 0)
        self._addNumberProperty('position', 0)
        self._addNumberProperty('rewardId', 0)
        self._addResourceProperty('bgImage', R.invalid())
        self.onLeaderboardBtnClick = self._addCommand('onLeaderboardBtnClick')