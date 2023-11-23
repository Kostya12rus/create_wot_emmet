# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/reward_item_model.py
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class RewardItemModel(BonusModel):
    __slots__ = ()
    SIZE_ADAPTIVE = 0
    SIZE_SMALL = 1
    SIZE_BIG = 2

    def __init__(self, properties=15, commands=0):
        super(RewardItemModel, self).__init__(properties=properties, commands=commands)

    def getItem(self):
        return self._getString(7)

    def setItem(self, value):
        self._setString(7, value)

    def getUserName(self):
        return self._getString(8)

    def setUserName(self, value):
        self._setString(8, value)

    def getIcon(self):
        return self._getString(9)

    def setIcon(self, value):
        self._setString(9, value)

    def getType(self):
        return self._getString(10)

    def setType(self, value):
        self._setString(10, value)

    def getBigIcon(self):
        return self._getString(11)

    def setBigIcon(self, value):
        self._setString(11, value)

    def getOverlayType(self):
        return self._getString(12)

    def setOverlayType(self, value):
        self._setString(12, value)

    def getIsCollectionEntity(self):
        return self._getBool(13)

    def setIsCollectionEntity(self, value):
        self._setBool(13, value)

    def getItemType(self):
        return self._getNumber(14)

    def setItemType(self, value):
        self._setNumber(14, value)

    def _initialize(self):
        super(RewardItemModel, self)._initialize()
        self._addStringProperty('item', '')
        self._addStringProperty('userName', '')
        self._addStringProperty('icon', '')
        self._addStringProperty('type', '')
        self._addStringProperty('bigIcon', '')
        self._addStringProperty('overlayType', '')
        self._addBoolProperty('isCollectionEntity', False)
        self._addNumberProperty('itemType', 0)