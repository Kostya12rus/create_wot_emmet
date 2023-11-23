# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SimpleDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SimpleDialogMeta(AbstractWindowView):

    def onButtonClick(self, buttonId):
        self._printOverrideError('onButtonClick')

    def as_setTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(text)

    def as_setTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)

    def as_setButtonsS(self, buttonNames):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtons(buttonNames)

    def as_setButtonEnablingS(self, id, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonEnabling(id, isEnabled)

    def as_setButtonFocusS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonFocus(id)