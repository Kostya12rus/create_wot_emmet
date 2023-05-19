# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/bootcamp/rewards_tooltip.py
from frameworks.wulf.view.view import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.bootcamp.bootcamp_rewards_tooltip_model import BootcampRewardsTooltipModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IBootcampController

class RewardsTooltip(ViewImpl):
    __slots__ = ()
    __bootcampController = dependency.descriptor(IBootcampController)

    def __init__(self, isNeedAwarding):
        settings = ViewSettings(R.views.lobby.bootcamp.RewardsTooltip(), model=BootcampRewardsTooltipModel())
        super(RewardsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(RewardsTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(RewardsTooltip, self)._onLoading(*args, **kwargs)
        self.viewModel.setIsNeedAwarding(self.__bootcampController.needAwarding())