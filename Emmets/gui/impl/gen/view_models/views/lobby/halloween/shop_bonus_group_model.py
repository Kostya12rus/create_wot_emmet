# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/shop_bonus_group_model.py
from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class BonusGroupTypeEnum(Enum):
    PREMIUM = 'premium'
    CUSTOMIZATIONS = 'customizations'
    KEYS = 'keys'
    VEHICLES = 'vehicles'
    BONUS_ITEMS = 'bonus_items'


class ShopBonusGroupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ShopBonusGroupModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return BonusGroupTypeEnum(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getBonusItems(self):
        return self._getArray(1)

    def setBonusItems(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(ShopBonusGroupModel, self)._initialize()
        self._addStringProperty('type')
        self._addArrayProperty('bonusItems', Array())