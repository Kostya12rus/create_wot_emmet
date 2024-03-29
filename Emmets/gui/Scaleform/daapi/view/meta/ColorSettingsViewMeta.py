# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ColorSettingsViewMeta.py
from gui.Scaleform.framework.entities.View import View

class ColorSettingsViewMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onApply(self, diff):
        self._printOverrideError('onApply')

    def onReset(self):
        self._printOverrideError('onReset')

    def onSettingsChange(self, settingName, settingValue):
        self._printOverrideError('onSettingsChange')

    def onTabSelected(self, selectedTab):
        self._printOverrideError('onTabSelected')

    def setViewWidth(self, value):
        self._printOverrideError('setViewWidth')

    def moveSpace(self, x, y, delta):
        self._printOverrideError('moveSpace')

    def as_initDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_initData(data)

    def as_updateDataS(self, selectedTab, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateData(selectedTab, data)