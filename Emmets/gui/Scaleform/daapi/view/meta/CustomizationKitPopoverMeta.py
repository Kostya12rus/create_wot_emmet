# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationKitPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationKitPopoverMeta(SmartPopOverView):

    def removeCustomizationKit(self):
        self._printOverrideError('removeCustomizationKit')

    def updateAutoProlongation(self):
        self._printOverrideError('updateAutoProlongation')

    def as_setHeaderS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(title)

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()

    def as_showClearMessageS(self, isClear, message):
        if self._isDAAPIInited():
            return self.flashObject.as_showClearMessage(isClear, message)

    def as_setAutoProlongationCheckboxSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoProlongationCheckboxSelected(value)

    def as_setAutoProlongationCheckboxEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoProlongationCheckboxEnabled(value)