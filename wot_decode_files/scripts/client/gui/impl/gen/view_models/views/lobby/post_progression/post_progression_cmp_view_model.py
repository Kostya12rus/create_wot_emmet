# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_cmp_view_model.py
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import PostProgressionBaseViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_compare_model import PostProgressionCompareModel

class PostProgressionCmpViewModel(PostProgressionBaseViewModel):
    __slots__ = ('onExitAction', )

    def __init__(self, properties=6, commands=2):
        super(PostProgressionCmpViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def compareControl(self):
        return self._getViewModel(5)

    @staticmethod
    def getCompareControlType():
        return PostProgressionCompareModel

    def _initialize(self):
        super(PostProgressionCmpViewModel, self)._initialize()
        self._addViewModelProperty('compareControl', PostProgressionCompareModel())
        self.onExitAction = self._addCommand('onExitAction')