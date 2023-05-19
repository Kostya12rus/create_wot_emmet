# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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