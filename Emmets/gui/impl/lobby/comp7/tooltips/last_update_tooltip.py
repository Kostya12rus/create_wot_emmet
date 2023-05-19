# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/tooltips/last_update_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.last_update_tooltip_model import LastUpdateTooltipModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class LastUpdateTooltip(ViewImpl):
    __slots__ = ()
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.comp7.tooltips.LastUpdateTooltip())
        settings.model = LastUpdateTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(LastUpdateTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(LastUpdateTooltip, self).getViewModel()

    def _onLoading(self, description, updateTime=None, *args, **kwargs):
        super(LastUpdateTooltip, self)._onLoading(*args, **kwargs)
        self.viewModel.setDescription(description)
        self.viewModel.setLeaderboardUpdateTimestamp(updateTime)