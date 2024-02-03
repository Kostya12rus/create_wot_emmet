# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_battle_royale_model.py
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_battle_royale_widget_model import ModeSelectorBattleRoyaleWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel

class ModeSelectorBattleRoyaleModel(ModeSelectorNormalCardModel):
    __slots__ = ()

    def __init__(self, properties=21, commands=0):
        super(ModeSelectorBattleRoyaleModel, self).__init__(properties=properties, commands=commands)

    @property
    def widget(self):
        return self._getViewModel(20)

    @staticmethod
    def getWidgetType():
        return ModeSelectorBattleRoyaleWidgetModel

    def _initialize(self):
        super(ModeSelectorBattleRoyaleModel, self)._initialize()
        self._addViewModelProperty('widget', ModeSelectorBattleRoyaleWidgetModel())