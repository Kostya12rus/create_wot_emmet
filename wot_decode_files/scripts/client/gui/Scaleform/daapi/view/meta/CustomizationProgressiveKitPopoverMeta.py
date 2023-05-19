# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationProgressiveKitPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationProgressiveKitPopoverMeta(SmartPopOverView):

    def remove(self, id, itemsList, seasonType):
        self._printOverrideError('remove')

    def removeAll(self):
        self._printOverrideError('removeAll')

    def setToDefault(self):
        self._printOverrideError('setToDefault')

    def onFilterChanged(self, showHistoric, showNonHistoric, showFantastic, showProgressiveLocked):
        self._printOverrideError('onFilterChanged')

    def as_setHeaderS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(value)

    def as_showClearMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_showClearMessage(message)

    def as_setDefaultButtonEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultButtonEnabled(value)

    def as_setItemsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setItems(value)