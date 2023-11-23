# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileTechniqueMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileTechniqueMeta(ProfileSection):

    def setSelectedTableColumn(self, index, sortDirection):
        self._printOverrideError('setSelectedTableColumn')

    def setSeason(self, seasonId):
        self._printOverrideError('setSeason')

    def showVehiclesRating(self):
        self._printOverrideError('showVehiclesRating')

    def as_responseVehicleDossierS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_responseVehicleDossier(data)

    def as_setRatingButtonS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRatingButton(data)

    def as_setBtnCountersS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_setBtnCounters(counters)

    def as_setPrestigeVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrestigeVisible(value)