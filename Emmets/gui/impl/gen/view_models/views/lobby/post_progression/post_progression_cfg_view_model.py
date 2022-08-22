# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_cfg_view_model.py
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import PostProgressionBaseViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_purchase_model import PostProgressionPurchaseModel

class PostProgressionCfgViewModel(PostProgressionBaseViewModel):
    __slots__ = ('onGoBackAction', 'onResearchAction')

    def __init__(self, properties=6, commands=3):
        super(PostProgressionCfgViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def purchasePreview(self):
        return self._getViewModel(5)

    @staticmethod
    def getPurchasePreviewType():
        return PostProgressionPurchaseModel

    def _initialize(self):
        super(PostProgressionCfgViewModel, self)._initialize()
        self._addViewModelProperty('purchasePreview', PostProgressionPurchaseModel())
        self.onGoBackAction = self._addCommand('onGoBackAction')
        self.onResearchAction = self._addCommand('onResearchAction')