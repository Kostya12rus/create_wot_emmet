# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mapbox/map_box_awards_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.mapbox.reward_item_model import RewardItemModel

class MapBoxAwardsViewModel(ViewModel):
    __slots__ = ('onPick', )

    def __init__(self, properties=2, commands=1):
        super(MapBoxAwardsViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getBattlesNumber(self):
        return self._getNumber(1)

    def setBattlesNumber(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(MapBoxAwardsViewModel, self)._initialize()
        self._addViewModelProperty('rewards', UserListModel())
        self._addNumberProperty('battlesNumber', 0)
        self.onPick = self._addCommand('onPick')