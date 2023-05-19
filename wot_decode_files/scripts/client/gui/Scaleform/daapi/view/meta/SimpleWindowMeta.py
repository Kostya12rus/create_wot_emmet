# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SimpleWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SimpleWindowMeta(AbstractWindowView):

    def onBtnClick(self, action):
        self._printOverrideError('onBtnClick')

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_setTextS(self, header, descrition):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(header, descrition)

    def as_setImageS(self, imgPath, imgBottomMargin):
        if self._isDAAPIInited():
            return self.flashObject.as_setImage(imgPath, imgBottomMargin)

    def as_setButtonsS(self, buttonsList, align, btnWidth):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtons(buttonsList, align, btnWidth)