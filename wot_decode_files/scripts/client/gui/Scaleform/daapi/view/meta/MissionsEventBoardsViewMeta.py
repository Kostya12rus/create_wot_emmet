# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsEventBoardsViewMeta.py
from gui.Scaleform.daapi.view.lobby.missions.regular.missions_page import ElenMissionView

class MissionsEventBoardsViewMeta(ElenMissionView):

    def openBoardView(self):
        self._printOverrideError('openBoardView')

    def participateClick(self, eventID):
        self._printOverrideError('participateClick')

    def orderClick(self, eventID):
        self._printOverrideError('orderClick')

    def techniqueClick(self, eventID):
        self._printOverrideError('techniqueClick')

    def awardClick(self, eventID):
        self._printOverrideError('awardClick')

    def registrationClick(self, eventID):
        self._printOverrideError('registrationClick')

    def serverClick(self, eventID, server):
        self._printOverrideError('serverClick')

    def expand(self, id, value):
        self._printOverrideError('expand')

    def as_setMaintenanceS(self, visible, message1, message2, buttonLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaintenance(visible, message1, message2, buttonLabel)

    def as_setPlayFadeInTweenEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayFadeInTweenEnabled(value)