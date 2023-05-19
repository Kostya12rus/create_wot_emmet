# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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