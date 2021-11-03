# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsLinkedSetViewMeta.py
from gui.Scaleform.daapi.view.lobby.missions.regular.missions_page import LinkedSetMissionView

class MissionsLinkedSetViewMeta(LinkedSetMissionView):

    def useTokenClick(self, eventID):
        self._printOverrideError('useTokenClick')

    def expand(self, id, value):
        self._printOverrideError('expand')

    def as_setMaintenanceS(self, visible, message1, message2, buttonLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaintenance(visible, message1, message2, buttonLabel)

    def as_setPlayFadeInTweenEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayFadeInTweenEnabled(value)