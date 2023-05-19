# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic/super_platoon_panel.py
from gui.Scaleform.daapi.view.meta.SuperPlatoonPanelMeta import SuperPlatoonPanelMeta
from helpers import i18n
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE
_MAX_INVITES_DISPLAYED = 4

class SuperPlatoonPanel(SuperPlatoonPanelMeta):

    def _populate(self):
        super(SuperPlatoonPanel, self)._populate()
        self.as_setPlatoonTitleS(i18n.makeString(EPIC_BATTLE.SUPER_PLATOON_PANEL_TITLE))
        self.as_setMaxDisplayedInviteMessagesS(_MAX_INVITES_DISPLAYED)

    def _handleNextMode(self, _):
        pass