# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tooltips/clans.py
from frameworks.wulf import View, ViewFlags, ViewSettings
from gui.impl.gen.view_models.views.lobby.tooltips.clan_short_info_content_model import ClanShortInfoContentModel
from gui.shared.view_helpers.emblems import ClanEmblemsHelper
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.web import IWebController

class ClanShortInfoTooltipContent(View, ClanEmblemsHelper):
    __webCtrl = dependency.descriptor(IWebController)

    def __init__(self):
        settings = ViewSettings(R.views.lobby.tooltips.clans.ClanShortInfoTooltipContent(), ViewFlags.COMPONENT, ClanShortInfoContentModel())
        super(ClanShortInfoTooltipContent, self).__init__(settings)
        clanProfile = self.__webCtrl.getAccountProfile()
        self.requestClanEmblem32x32(clanProfile.getClanDbID())
        self.viewModel.setFullName(clanProfile.getClanFullName())

    @property
    def viewModel(self):
        return super(ClanShortInfoTooltipContent, self).getViewModel()

    def onClanEmblem32x32Received(self, clanDbID, emblem):
        if emblem and self.viewModel and self.viewModel.isBound():
            self.viewModel.setEmblem(self.getMemoryTexturePath(emblem))