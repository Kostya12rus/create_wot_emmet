# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/tooltips/setup_tab_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.setup_tab_tooltip_view_model import SetupTabTooltipViewModel
from gui.impl.pub import ViewImpl

class SetupTabTooltipView(ViewImpl):

    def __init__(self, name):
        settings = ViewSettings(R.views.lobby.tanksetup.tooltips.SetupTabTooltipView())
        settings.model = SetupTabTooltipViewModel()
        settings.args = (name,)
        super(SetupTabTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SetupTabTooltipView, self).getViewModel()

    def _onLoading(self, name, *args, **kwargs):
        super(SetupTabTooltipView, self)._onLoading(*args, **kwargs)
        self.viewModel.setName(name)