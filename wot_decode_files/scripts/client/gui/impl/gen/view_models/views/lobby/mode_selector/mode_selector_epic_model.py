# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_epic_model.py
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_epic_widget_model import ModeSelectorEpicWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel

class ModeSelectorEpicModel(ModeSelectorNormalCardModel):
    __slots__ = ()

    def __init__(self, properties=21, commands=0):
        super(ModeSelectorEpicModel, self).__init__(properties=properties, commands=commands)

    @property
    def widget(self):
        return self._getViewModel(20)

    @staticmethod
    def getWidgetType():
        return ModeSelectorEpicWidgetModel

    def _initialize(self):
        super(ModeSelectorEpicModel, self)._initialize()
        self._addViewModelProperty('widget', ModeSelectorEpicWidgetModel())