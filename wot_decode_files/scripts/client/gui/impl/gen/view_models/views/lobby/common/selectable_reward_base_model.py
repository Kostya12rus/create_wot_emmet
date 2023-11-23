# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/selectable_reward_base_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_model import SelectableRewardModel

class SelectableRewardBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SelectableRewardBaseModel, self).__init__(properties=properties, commands=commands)

    @property
    def selectableRewardModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getSelectableRewardModelType():
        return SelectableRewardModel

    def _initialize(self):
        super(SelectableRewardBaseModel, self)._initialize()
        self._addViewModelProperty('selectableRewardModel', SelectableRewardModel())