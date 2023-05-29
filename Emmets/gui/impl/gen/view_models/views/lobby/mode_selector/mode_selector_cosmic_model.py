# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_cosmic_model.py
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_cosmic_widget_model import ModeSelectorCosmicWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel

class ModeSelectorCosmicModel(ModeSelectorNormalCardModel):
    __slots__ = ()

    def __init__(self, properties=22, commands=0):
        super(ModeSelectorCosmicModel, self).__init__(properties=properties, commands=commands)

    @property
    def widget(self):
        return self._getViewModel(20)

    @staticmethod
    def getWidgetType():
        return ModeSelectorCosmicWidgetModel

    def getIsSuspended(self):
        return self._getBool(21)

    def setIsSuspended(self, value):
        self._setBool(21, value)

    def _initialize(self):
        super(ModeSelectorCosmicModel, self)._initialize()
        self._addViewModelProperty('widget', ModeSelectorCosmicWidgetModel())
        self._addBoolProperty('isSuspended', False)