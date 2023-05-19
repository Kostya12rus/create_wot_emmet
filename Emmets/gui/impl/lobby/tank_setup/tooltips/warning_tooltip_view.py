# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/tooltips/warning_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.warning_tooltip_view_model import WarningTooltipViewModel, WarningDescription
from gui.impl.pub import ViewImpl

class WarningTooltipView(ViewImpl):

    def __init__(self, reason, isCritical):
        settings = ViewSettings(R.views.lobby.tanksetup.tooltips.WarningTooltipView())
        settings.model = WarningTooltipViewModel()
        settings.args = (reason, isCritical)
        super(WarningTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(WarningTooltipView, self).getViewModel()

    def _onLoading(self, reason, isCritical, *args, **kwargs):
        super(WarningTooltipView, self)._onLoading(*args, **kwargs)
        self.viewModel.setReason(WarningDescription(reason))
        self.viewModel.setIsCritical(isCritical)