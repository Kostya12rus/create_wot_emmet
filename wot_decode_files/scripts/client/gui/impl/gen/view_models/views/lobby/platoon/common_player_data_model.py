# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/common_player_data_model.py
from frameworks.wulf import ViewModel

class CommonPlayerDataModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CommonPlayerDataModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getClanTag(self):
        return self._getString(1)

    def setClanTag(self, value):
        self._setString(1, value)

    def getBadgeID(self):
        return self._getString(2)

    def setBadgeID(self, value):
        self._setString(2, value)

    def getRating(self):
        return self._getString(3)

    def setRating(self, value):
        self._setString(3, value)

    def getColor(self):
        return self._getString(4)

    def setColor(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(CommonPlayerDataModel, self)._initialize()
        self._addStringProperty('name', 'rookie')
        self._addStringProperty('clanTag', '')
        self._addStringProperty('badgeID', '')
        self._addStringProperty('rating', '')
        self._addStringProperty('color', '')