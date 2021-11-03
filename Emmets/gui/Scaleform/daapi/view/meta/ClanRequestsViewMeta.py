# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanRequestsViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesWindowAbstractTabView import ClanInvitesWindowAbstractTabView

class ClanRequestsViewMeta(ClanInvitesWindowAbstractTabView):

    def acceptRequest(self, dbId):
        self._printOverrideError('acceptRequest')

    def declineRequest(self, dbId):
        self._printOverrideError('declineRequest')

    def sendInvite(self, dbId):
        self._printOverrideError('sendInvite')