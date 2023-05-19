# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/reward_window_content_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class RewardWindowContentModel(ViewModel):
    __slots__ = ('onConfirmBtnClicked', 'onSecondBtnClicked', 'onHyperLinkClicked')

    def __init__(self, properties=3, commands=3):
        super(RewardWindowContentModel, self).__init__(properties=properties, commands=commands)

    @property
    def rewardsList(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsListType():
        return ListModel

    def getEventName(self):
        return self._getString(1)

    def setEventName(self, value):
        self._setString(1, value)

    def getShowRewards(self):
        return self._getBool(2)

    def setShowRewards(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(RewardWindowContentModel, self)._initialize()
        self._addViewModelProperty('rewardsList', ListModel())
        self._addStringProperty('eventName', '')
        self._addBoolProperty('showRewards', False)
        self.onConfirmBtnClicked = self._addCommand('onConfirmBtnClicked')
        self.onSecondBtnClicked = self._addCommand('onSecondBtnClicked')
        self.onHyperLinkClicked = self._addCommand('onHyperLinkClicked')