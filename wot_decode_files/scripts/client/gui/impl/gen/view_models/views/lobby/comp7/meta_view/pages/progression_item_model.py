# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/meta_view/pages/progression_item_model.py
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.progression_item_base_model import ProgressionItemBaseModel

class ProgressionItemModel(ProgressionItemBaseModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ProgressionItemModel, self).__init__(properties=properties, commands=commands)

    def getHasRankInactivity(self):
        return self._getBool(4)

    def setHasRankInactivity(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(ProgressionItemModel, self)._initialize()
        self._addBoolProperty('hasRankInactivity', False)