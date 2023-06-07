# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/achievements/tooltips/editing_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.achievements.tooltips.editing_tooltip_view_model import EditingTooltipViewModel, TooltipType
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class EditingTooltip(ViewImpl):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, tooltipType):
        settings = ViewSettings(R.views.lobby.achievements.tooltips.EditingTooltip(), model=EditingTooltipViewModel())
        self.__tooltipType = tooltipType
        super(EditingTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(EditingTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(EditingTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            model.setTooltipType(self.__getTooltipType())
            model.setRequiredAchievementsCount(self.__lobbyContext.getServerSettings().getAchievements20GeneralConfig().getLayoutLength() + 1)

    def _finalize(self):
        self.__tooltipType = None
        super(EditingTooltip, self)._finalize()
        return

    def __getTooltipType(self):
        if TooltipType.NOT_ENOUGH_ACHIEVEMENTS.value == self.__tooltipType:
            return TooltipType.NOT_ENOUGH_ACHIEVEMENTS
        if TooltipType.DISABLED.value == self.__tooltipType:
            return TooltipType.DISABLED
        if TooltipType.DISABLED_LAYOUT.value == self.__tooltipType:
            return TooltipType.DISABLED_LAYOUT
        if TooltipType.OTHER_PLAYER.value == self.__tooltipType:
            return TooltipType.OTHER_PLAYER