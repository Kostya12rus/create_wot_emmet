# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileStatisticsMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileStatisticsMeta(ProfileSection):

    def getData(self, data):
        self._printOverrideError('getData')

    def setSeason(self, seasonId):
        self._printOverrideError('setSeason')

    def showPlayersStats(self):
        self._printOverrideError('showPlayersStats')

    def as_updatePlayerStatsBtnS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerStatsBtn(isVisible)