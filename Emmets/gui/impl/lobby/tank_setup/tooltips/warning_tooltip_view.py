# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/tooltips/warning_tooltip_view.py
import typing
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.warning_tooltip_view_model import WarningTooltipViewModel
from gui.impl.pub import ViewImpl
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.warning_tooltip_view_model import WarningDescription

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
        self.viewModel.setReason(reason)
        self.viewModel.setIsCritical(isCritical)