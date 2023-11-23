# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventBasesPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventBasesPanelMeta(BaseDAAPIComponent):

    def as_setBase1IDS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_setBase1ID(id)

    def as_setBase2IDS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_setBase2ID(id)

    def as_setBase1StateS(self, owningTeam, attackingTeam):
        if self._isDAAPIInited():
            return self.flashObject.as_setBase1State(owningTeam, attackingTeam)

    def as_setBase2StateS(self, owningTeam, attackingTeam):
        if self._isDAAPIInited():
            return self.flashObject.as_setBase2State(owningTeam, attackingTeam)

    def as_setBase1ProgressS(self, progress, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setBase1Progress(progress, time)

    def as_setBase2ProgressS(self, progress, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setBase2Progress(progress, time)

    def as_setVisibilityS(self, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisibility(vis)

    def as_setColorBlindS(self, isBlind):
        if self._isDAAPIInited():
            return self.flashObject.as_setColorBlind(isBlind)