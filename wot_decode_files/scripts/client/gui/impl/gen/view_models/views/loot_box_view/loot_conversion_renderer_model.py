# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/loot_conversion_renderer_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.loot_box_view.loot_animated_renderer_model import LootAnimatedRendererModel

class LootConversionRendererModel(LootAnimatedRendererModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(LootConversionRendererModel, self).__init__(properties=properties, commands=commands)

    def getIconFrom(self):
        return self._getResource(16)

    def setIconFrom(self, value):
        self._setResource(16, value)

    def _initialize(self):
        super(LootConversionRendererModel, self)._initialize()
        self._addResourceProperty('iconFrom', R.invalid())