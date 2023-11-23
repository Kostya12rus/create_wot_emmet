# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/loot_compensation_renderer_model.py
from gui.impl.gen.view_models.views.loot_box_view.loot_animated_renderer_model import LootAnimatedRendererModel

class LootCompensationRendererModel(LootAnimatedRendererModel):
    __slots__ = ()

    def __init__(self, properties=25, commands=0):
        super(LootCompensationRendererModel, self).__init__(properties=properties, commands=commands)

    def getIconFrom(self):
        return self._getString(16)

    def setIconFrom(self, value):
        self._setString(16, value)

    def getLabelBeforeStr(self):
        return self._getString(17)

    def setLabelBeforeStr(self, value):
        self._setString(17, value)

    def getIconBefore(self):
        return self._getString(18)

    def setIconBefore(self, value):
        self._setString(18, value)

    def getIconAfter(self):
        return self._getString(19)

    def setIconAfter(self, value):
        self._setString(19, value)

    def getLabelBefore(self):
        return self._getString(20)

    def setLabelBefore(self, value):
        self._setString(20, value)

    def getLabelAfter(self):
        return self._getString(21)

    def setLabelAfter(self, value):
        self._setString(21, value)

    def getBonusName(self):
        return self._getString(22)

    def setBonusName(self, value):
        self._setString(22, value)

    def getCountBefore(self):
        return self._getNumber(23)

    def setCountBefore(self, value):
        self._setNumber(23, value)

    def getLabelAlignAfter(self):
        return self._getString(24)

    def setLabelAlignAfter(self, value):
        self._setString(24, value)

    def _initialize(self):
        super(LootCompensationRendererModel, self)._initialize()
        self._addStringProperty('iconFrom', '')
        self._addStringProperty('labelBeforeStr', '')
        self._addStringProperty('iconBefore', '')
        self._addStringProperty('iconAfter', '')
        self._addStringProperty('labelBefore', '')
        self._addStringProperty('labelAfter', '')
        self._addStringProperty('bonusName', '')
        self._addNumberProperty('countBefore', 1)
        self._addStringProperty('labelAlignAfter', 'center')