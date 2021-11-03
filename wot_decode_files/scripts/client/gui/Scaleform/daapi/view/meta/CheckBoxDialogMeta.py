# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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