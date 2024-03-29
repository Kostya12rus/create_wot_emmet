# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/gf_drop_down_item.py
from frameworks.wulf import ViewModel

class GfDropDownItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(GfDropDownItem, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getLabel(self):
        return self._getString(1)

    def setLabel(self, value):
        self._setString(1, value)

    def getIsDisabled(self):
        return self._getBool(2)

    def setIsDisabled(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(GfDropDownItem, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('label', '')
        self._addBoolProperty('isDisabled', False)