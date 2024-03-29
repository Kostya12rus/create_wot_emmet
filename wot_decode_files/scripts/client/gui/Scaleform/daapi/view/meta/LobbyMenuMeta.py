# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyMenuMeta.py
from gui.Scaleform.framework.entities.View import View

class LobbyMenuMeta(View):

    def settingsClick(self):
        self._printOverrideError('settingsClick')

    def cancelClick(self):
        self._printOverrideError('cancelClick')

    def refuseTraining(self):
        self._printOverrideError('refuseTraining')

    def logoffClick(self):
        self._printOverrideError('logoffClick')

    def quitClick(self):
        self._printOverrideError('quitClick')

    def postClick(self):
        self._printOverrideError('postClick')

    def onCounterNeedUpdate(self):
        self._printOverrideError('onCounterNeedUpdate')

    def bootcampClick(self):
        self._printOverrideError('bootcampClick')

    def onEscapePress(self):
        self._printOverrideError('onEscapePress')

    def manualClick(self):
        self._printOverrideError('manualClick')

    def as_setVersionMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setVersionMessage(message)

    def as_setCounterS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_setCounter(counters)

    def as_removeCounterS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_removeCounter(counters)

    def as_setBootcampButtonLabelS(self, label, icon):
        if self._isDAAPIInited():
            return self.flashObject.as_setBootcampButtonLabel(label, icon)

    def as_setPostButtonIconsS(self, iconClose, iconOpen):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostButtonIcons(iconClose, iconOpen)

    def as_setPostButtonVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostButtonVisible(isVisible)

    def as_showBootcampButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showBootcampButton(value)

    def as_showManualButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showManualButton(value)

    def as_setManualButtonIconS(self, icon):
        if self._isDAAPIInited():
            return self.flashObject.as_setManualButtonIcon(icon)

    def as_setMenuStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setMenuState(state)