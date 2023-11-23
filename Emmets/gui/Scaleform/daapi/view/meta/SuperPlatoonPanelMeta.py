# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SuperPlatoonPanelMeta.py
from gui.Scaleform.daapi.view.battle.classic.players_panel import PlayersPanel

class SuperPlatoonPanelMeta(PlayersPanel):

    def as_setPlatoonTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlatoonTitle(title)

    def as_setMaxDisplayedInviteMessagesS(self, maxInvites):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxDisplayedInviteMessages(maxInvites)