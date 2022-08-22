# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LinkedSetDetailsOverlayMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class LinkedSetDetailsOverlayMeta(BaseDAAPIComponent):

    def startClick(self, eventID):
        self._printOverrideError('startClick')

    def setPage(self, pageID):
        self._printOverrideError('setPage')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setDataVideoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDataVideo(data)

    def as_setColorPagesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setColorPages(data)

    def as_setPageS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setPage(index)