# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/shop_view_model.py
from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.halloween.shop_bundle_model import ShopBundleModel

class PageTypeEnum(Enum):
    KEYS = 'keys'
    VEHICLES = 'vehicles'


class ShopViewModel(ViewModel):
    __slots__ = ('onBuyClick', 'onClose')

    def __init__(self, properties=2, commands=2):
        super(ShopViewModel, self).__init__(properties=properties, commands=commands)

    def getPageType(self):
        return PageTypeEnum(self._getString(0))

    def setPageType(self, value):
        self._setString(0, value.value)

    def getBundles(self):
        return self._getArray(1)

    def setBundles(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(ShopViewModel, self)._initialize()
        self._addStringProperty('pageType')
        self._addArrayProperty('bundles', Array())
        self.onBuyClick = self._addCommand('onBuyClick')
        self.onClose = self._addCommand('onClose')