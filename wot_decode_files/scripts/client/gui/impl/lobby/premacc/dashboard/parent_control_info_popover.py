# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/premacc/dashboard/parent_control_info_popover.py
from adisp import adisp_process
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.premacc.dashboard.parent_control_info_popover_model import ParentControlInfoPopoverModel
from gui.impl.pub import PopOverViewImpl
from helpers import dependency
from skeletons.gui.game_control import IExternalLinksController
_PARENT_CONTROL_HELP_URL = 'parentControlHelpURL'

class ParentControlInfoPopoverContent(PopOverViewImpl):
    __slots__ = ()
    __links = dependency.descriptor(IExternalLinksController)

    def __init__(self):
        settings = ViewSettings(R.views.lobby.premacc.dashboard.prem_dashboard_parent_control_info.PremDashboardParentControlInfoContent())
        settings.model = ParentControlInfoPopoverModel()
        super(ParentControlInfoPopoverContent, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ParentControlInfoPopoverContent, self).getViewModel()

    def _initialize(self):
        super(ParentControlInfoPopoverContent, self)._initialize()
        self.viewModel.onLinkClicked += self.__onLinkClicked

    def _finalize(self):
        self.viewModel.onLinkClicked -= self.__onLinkClicked

    @adisp_process
    def __onLinkClicked(self):
        parsedUrl = yield self.__links.getURL(_PARENT_CONTROL_HELP_URL)
        self.__links.open(parsedUrl)