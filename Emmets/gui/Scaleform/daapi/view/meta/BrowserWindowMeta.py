# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BrowserWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BrowserWindowMeta(AbstractWindowView):

    def as_configureS(self, title, showActionBtn, showCloseBtn, isSolidBorder):
        if self._isDAAPIInited():
            return self.flashObject.as_configure(title, showActionBtn, showCloseBtn, isSolidBorder)

    def as_setSizeS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(width, height)