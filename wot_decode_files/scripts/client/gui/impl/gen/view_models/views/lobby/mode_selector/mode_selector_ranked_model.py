# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_ranked_model.py
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_ranked_widget_model import ModeSelectorRankedWidgetModel

class ModeSelectorRankedModel(ModeSelectorNormalCardModel):
    __slots__ = ()

    def __init__(self, properties=22, commands=0):
        super(ModeSelectorRankedModel, self).__init__(properties=properties, commands=commands)

    @property
    def widget(self):
        return self._getViewModel(21)

    @staticmethod
    def getWidgetType():
        return ModeSelectorRankedWidgetModel

    def _initialize(self):
        super(ModeSelectorRankedModel, self)._initialize()
        self._addViewModelProperty('widget', ModeSelectorRankedWidgetModel())