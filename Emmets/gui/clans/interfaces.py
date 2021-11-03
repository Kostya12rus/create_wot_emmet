# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/clans/interfaces.py


class IClanListener(object):

    def onClanEnableChanged(self, enabled):
        pass

    def onClanInvitesCountReceived(self, clanDbID, invitesCount):
        pass

    def onClanAppsCountReceived(self, clanDbID, appsCount):
        pass

    def onClanInfoReceived(self, clanDbID, clanInfo):
        pass

    def onClanWebVitalInfoChanged(self, clanDbID, fieldName, value):
        pass

    def onAccountClanProfileChanged(self, profile):
        pass

    def onAccountClanInfoReceived(self, info):
        pass

    def onAccountInvitesReceived(self, invites):
        pass

    def onAccountAppsReceived(self, applications):
        pass

    def onAccountWebVitalInfoChanged(self, fieldName, value):
        pass

    def onClanAppStateChanged(self, appId, state):
        pass

    def onClanInvitesStateChanged(self, inviteIds, state):
        pass

    def onWgncNotificationReceived(self, notifID, item):
        pass

    def onMembersListChanged(self, members):
        pass