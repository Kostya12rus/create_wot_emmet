# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CheckBoxDialogMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CheckBoxDialogMeta(BaseDAAPIComponent):

    def onCheckBoxChange(self, isSelected):
        self._printOverrideError('onCheckBoxChange')

    def as_setCheckBoxLabelS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxLabel(value)

    def as_setCheckBoxSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxSelected(value)

    def as_setCheckBoxEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxEnabled(value)