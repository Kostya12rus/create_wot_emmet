# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PaginationMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PaginationMeta(BaseDAAPIComponent):

    def showPage(self, dir):
        self._printOverrideError('showPage')

    def as_setPageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPage(value)

    def as_setEnabledS(self, leftEnabled, rightEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabled(leftEnabled, rightEnabled)