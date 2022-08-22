# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/confirmed_item_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class ConfirmedItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ConfirmedItemModel, self).__init__(properties=properties, commands=commands)

    @property
    def demountPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getDemountPriceType():
        return PriceModel

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def getImageSource(self):
        return self._getResource(2)

    def setImageSource(self, value):
        self._setResource(2, value)

    def getOverlayType(self):
        return self._getString(3)

    def setOverlayType(self, value):
        self._setString(3, value)

    def getHighlightType(self):
        return self._getString(4)

    def setHighlightType(self, value):
        self._setString(4, value)

    def getCanUseDemountKit(self):
        return self._getBool(5)

    def setCanUseDemountKit(self, value):
        self._setBool(5, value)

    def getLevel(self):
        return self._getNumber(6)

    def setLevel(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(ConfirmedItemModel, self)._initialize()
        self._addViewModelProperty('demountPrice', PriceModel())
        self._addStringProperty('name', '')
        self._addResourceProperty('imageSource', R.invalid())
        self._addStringProperty('overlayType', '')
        self._addStringProperty('highlightType', '')
        self._addBoolProperty('canUseDemountKit', False)
        self._addNumberProperty('level', 0)