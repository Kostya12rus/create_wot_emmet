# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/frontline/rewards_selection_view_model.py
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_base_model import SelectableRewardBaseModel

class RewardsSelectionViewModel(SelectableRewardBaseModel):
    __slots__ = ('onLoadedView', )

    def __init__(self, properties=1, commands=1):
        super(RewardsSelectionViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(RewardsSelectionViewModel, self)._initialize()
        self.onLoadedView = self._addCommand('onLoadedView')