# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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