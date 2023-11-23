# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicSpectatorViewMeta.py
from gui.Scaleform.daapi.view.battle.shared.postmortem_panel import PostmortemPanel

class EpicSpectatorViewMeta(PostmortemPanel):

    def as_setFollowInfoTextS(self, folowText):
        if self._isDAAPIInited():
            return self.flashObject.as_setFollowInfoText(folowText)

    def as_changeModeS(self, mode):
        if self._isDAAPIInited():
            return self.flashObject.as_changeMode(mode)

    def as_focusOnVehicleS(self, focused):
        if self._isDAAPIInited():
            return self.flashObject.as_focusOnVehicle(focused)

    def as_setTimerS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(time)