# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IconPriceDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.IconDialog import IconDialog

class IconPriceDialogMeta(IconDialog):

    def as_setMessagePriceS(self, dialogData):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagePrice(dialogData)

    def as_setPriceLabelS(self, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setPriceLabel(label)

    def as_setOperationAllowedS(self, isAllowed):
        if self._isDAAPIInited():
            return self.flashObject.as_setOperationAllowed(isAllowed)