# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/base_ammunition_slot.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BaseAmmunitionSlot(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(BaseAmmunitionSlot, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)

    def getKeyName(self):
        return self._getString(2)

    def setKeyName(self, value):
        self._setString(2, value)

    def getImageSource(self):
        return self._getResource(3)

    def setImageSource(self, value):
        self._setResource(3, value)

    def getWithAttention(self):
        return self._getBool(4)

    def setWithAttention(self, value):
        self._setBool(4, value)

    def getIsInstalled(self):
        return self._getBool(5)

    def setIsInstalled(self, value):
        self._setBool(5, value)

    def getIsMountedMoreThanOne(self):
        return self._getBool(6)

    def setIsMountedMoreThanOne(self, value):
        self._setBool(6, value)

    def getItemInstalledSetupIdx(self):
        return self._getNumber(7)

    def setItemInstalledSetupIdx(self, value):
        self._setNumber(7, value)

    def getOverlayType(self):
        return self._getString(8)

    def setOverlayType(self, value):
        self._setString(8, value)

    def getHighlightType(self):
        return self._getString(9)

    def setHighlightType(self, value):
        self._setString(9, value)

    def getCategoryImgSource(self):
        return self._getResource(10)

    def setCategoryImgSource(self, value):
        self._setResource(10, value)

    def _initialize(self):
        super(BaseAmmunitionSlot, self)._initialize()
        self._addNumberProperty('id', 0)
        self._addNumberProperty('intCD', 0)
        self._addStringProperty('keyName', '')
        self._addResourceProperty('imageSource', R.invalid())
        self._addBoolProperty('withAttention', False)
        self._addBoolProperty('isInstalled', True)
        self._addBoolProperty('isMountedMoreThanOne', False)
        self._addNumberProperty('itemInstalledSetupIdx', -1)
        self._addStringProperty('overlayType', '')
        self._addStringProperty('highlightType', '')
        self._addResourceProperty('categoryImgSource', R.invalid())