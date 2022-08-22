# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationEditedKitPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationEditedKitPopoverMeta(SmartPopOverView):

    def remove(self, id, itemsList, seasonType):
        self._printOverrideError('remove')

    def removeAll(self):
        self._printOverrideError('removeAll')

    def setToDefault(self):
        self._printOverrideError('setToDefault')

    def as_setHeaderS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(value)

    def as_setHelpMessageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHelpMessage(value)

    def as_setDefaultButtonEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultButtonEnabled(value)

    def as_showClearMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_showClearMessage(message)

    def as_setItemsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setItems(value)