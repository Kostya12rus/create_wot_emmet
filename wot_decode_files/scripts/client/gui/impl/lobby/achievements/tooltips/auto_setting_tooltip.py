# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/achievements/tooltips/auto_setting_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.achievements.tooltips.auto_setting_tooltip_model import AutoSettingTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class AutoSettingTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.achievements.tooltips.AutoSettingTooltip())
        settings.model = AutoSettingTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(AutoSettingTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(AutoSettingTooltip, self).getViewModel()

    def _onLoading(self, isSwitchedOn):
        with self.viewModel.transaction() as (model):
            model.setIsSwitchedOn(isSwitchedOn)