# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/reward_renderer_model.py
from frameworks.wulf import ViewModel

class RewardRendererModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(RewardRendererModel, self).__init__(properties=properties, commands=commands)

    def getLabelStr(self):
        return self._getString(0)

    def setLabelStr(self, value):
        self._setString(0, value)

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)

    def getTooltipId(self):
        return self._getNumber(2)

    def setTooltipId(self, value):
        self._setNumber(2, value)

    def getHighlightType(self):
        return self._getString(3)

    def setHighlightType(self, value):
        self._setString(3, value)

    def getOverlayType(self):
        return self._getString(4)

    def setOverlayType(self, value):
        self._setString(4, value)

    def getHasCompensation(self):
        return self._getBool(5)

    def setHasCompensation(self, value):
        self._setBool(5, value)

    def getLabelAlign(self):
        return self._getString(6)

    def setLabelAlign(self, value):
        self._setString(6, value)

    def getIconSize(self):
        return self._getString(7)

    def setIconSize(self, value):
        self._setString(7, value)

    def _initialize(self):
        super(RewardRendererModel, self)._initialize()
        self._addStringProperty('labelStr', '')
        self._addStringProperty('icon', '')
        self._addNumberProperty('tooltipId', 0)
        self._addStringProperty('highlightType', '')
        self._addStringProperty('overlayType', '')
        self._addBoolProperty('hasCompensation', False)
        self._addStringProperty('labelAlign', 'center')
        self._addStringProperty('iconSize', 'small')