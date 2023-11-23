# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanPersonalInvitesViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesViewWithTable import ClanInvitesViewWithTable

class ClanPersonalInvitesViewMeta(ClanInvitesViewWithTable):

    def acceptInvite(self, dbID):
        self._printOverrideError('acceptInvite')

    def declineInvite(self, dbID):
        self._printOverrideError('declineInvite')

    def setInviteSelected(self, dbID, selected):
        self._printOverrideError('setInviteSelected')

    def setSelectAllInvitesCheckBoxSelected(self, selected):
        self._printOverrideError('setSelectAllInvitesCheckBoxSelected')

    def declineAllSelectedInvites(self):
        self._printOverrideError('declineAllSelectedInvites')

    def as_setDeclineAllSelectedInvitesStateS(self, text, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setDeclineAllSelectedInvitesState(text, enabled)

    def as_setSelectAllCheckboxStateS(self, selected, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectAllCheckboxState(selected, visible)