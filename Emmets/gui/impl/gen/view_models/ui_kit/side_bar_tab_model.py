# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/side_bar_tab_model.py
from frameworks.wulf import ViewModel

class SideBarTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(SideBarTabModel, self).__init__(properties=properties, commands=commands)

    def getAlias(self):
        return self._getString(0)

    def setAlias(self, value):
        self._setString(0, value)

    def getTooltipHeader(self):
        return self._getString(1)

    def setTooltipHeader(self, value):
        self._setString(1, value)

    def getTooltipBody(self):
        return self._getString(2)

    def setTooltipBody(self, value):
        self._setString(2, value)

    def getLinkage(self):
        return self._getString(3)

    def setLinkage(self, value):
        self._setString(3, value)

    def getIcon(self):
        return self._getString(4)

    def setIcon(self, value):
        self._setString(4, value)

    def getEnabled(self):
        return self._getBool(5)

    def setEnabled(self, value):
        self._setBool(5, value)

    def getUnseenCount(self):
        return self._getNumber(6)

    def setUnseenCount(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(SideBarTabModel, self)._initialize()
        self._addStringProperty('alias', '')
        self._addStringProperty('tooltipHeader', '')
        self._addStringProperty('tooltipBody', '')
        self._addStringProperty('linkage', '')
        self._addStringProperty('icon', '')
        self._addBoolProperty('enabled', True)
        self._addNumberProperty('unseenCount', 0)