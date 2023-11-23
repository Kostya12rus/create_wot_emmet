# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/legacy/listener.py
from gui.prb_control.entities.base.listener import IPrbListener

class ILegacyIntroListener(IPrbListener):

    def onLegacyListReceived(self, result):
        pass

    def onLegacyRosterReceived(self, prebattleID, iterator):
        pass


class ILegacyListener(ILegacyIntroListener):

    def onSettingUpdated(self, entity, settingName, settingValue):
        pass

    def onPropertyUpdated(self, entity, propertyName, propertyValue):
        pass

    def onTeamStatesReceived(self, entity, team1State, team2State):
        pass

    def onPlayerAdded(self, entity, playerInfo):
        pass

    def onPlayerRemoved(self, entity, playerInfo):
        pass

    def onRostersChanged(self, entity, rosters, full):
        pass

    def onPlayerTeamNumberChanged(self, entity, team):
        pass

    def onPlayerRosterChanged(self, entity, actorInfo, playerInfo):
        pass

    def onPlayerStateChanged(self, entity, roster, accountInfo):
        pass