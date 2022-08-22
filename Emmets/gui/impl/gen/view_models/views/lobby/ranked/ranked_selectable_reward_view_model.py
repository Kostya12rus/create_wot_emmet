# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/ranked/ranked_selectable_reward_view_model.py
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_base_model import SelectableRewardBaseModel

class RankedSelectableRewardViewModel(SelectableRewardBaseModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RankedSelectableRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getRewardType(self):
        return self._getString(1)

    def setRewardType(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(RankedSelectableRewardViewModel, self)._initialize()
        self._addStringProperty('rewardType', '')