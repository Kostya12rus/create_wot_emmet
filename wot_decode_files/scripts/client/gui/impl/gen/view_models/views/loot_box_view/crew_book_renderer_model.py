# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/crew_book_renderer_model.py
from gui.impl.gen.view_models.views.loot_box_view.congrats_view_model import CongratsViewModel
from gui.impl.gen.view_models.views.loot_box_view.loot_animated_renderer_model import LootAnimatedRendererModel

class CrewBookRendererModel(LootAnimatedRendererModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(CrewBookRendererModel, self).__init__(properties=properties, commands=commands)

    @property
    def congratsViewModel(self):
        return self._getViewModel(16)

    @staticmethod
    def getCongratsViewModelType():
        return CongratsViewModel

    def _initialize(self):
        super(CrewBookRendererModel, self)._initialize()
        self._addViewModelProperty('congratsViewModel', CongratsViewModel())