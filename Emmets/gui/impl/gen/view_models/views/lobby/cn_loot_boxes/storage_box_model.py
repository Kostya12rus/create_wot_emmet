# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/cn_loot_boxes/storage_box_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class BoxType(Enum):
    COMMON = 'china_common'
    PREMIUM = 'china_premium'


class StorageBoxModel(ViewModel):
    __slots__ = ('onOpen', )

    def __init__(self, properties=2, commands=1):
        super(StorageBoxModel, self).__init__(properties=properties, commands=commands)

    def getCount(self):
        return self._getNumber(0)

    def setCount(self, value):
        self._setNumber(0, value)

    def getType(self):
        return BoxType(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)

    def _initialize(self):
        super(StorageBoxModel, self)._initialize()
        self._addNumberProperty('count', 0)
        self._addStringProperty('type')
        self.onOpen = self._addCommand('onOpen')