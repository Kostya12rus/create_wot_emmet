# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/loot_new_year_fragments_renderer_model.py
from gui.impl.gen.view_models.views.loot_box_view.loot_def_renderer_model import LootDefRendererModel

class LootNewYearFragmentsRendererModel(LootDefRendererModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(LootNewYearFragmentsRendererModel, self).__init__(properties=properties, commands=commands)

    def getCount(self):
        return self._getNumber(14)

    def setCount(self, value):
        self._setNumber(14, value)

    def _initialize(self):
        super(LootNewYearFragmentsRendererModel, self)._initialize()
        self._addNumberProperty('count', 0)