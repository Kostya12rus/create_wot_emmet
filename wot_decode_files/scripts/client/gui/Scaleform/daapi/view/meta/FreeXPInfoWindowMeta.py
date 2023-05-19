# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FreeXPInfoWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FreeXPInfoWindowMeta(AbstractWindowView):

    def onSubmitButton(self):
        self._printOverrideError('onSubmitButton')

    def onCancelButton(self):
        self._printOverrideError('onCancelButton')

    def as_setSubmitLabelS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSubmitLabel(value)

    def as_setTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(value)

    def as_setTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(value)