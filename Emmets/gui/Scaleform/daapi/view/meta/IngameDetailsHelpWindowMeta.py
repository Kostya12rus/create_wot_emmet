# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IngameDetailsHelpWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameDetailsHelpWindowMeta(AbstractWindowView):

    def requestPageData(self, index):
        self._printOverrideError('requestPageData')

    def as_setPaginatorDataS(self, pages):
        if self._isDAAPIInited():
            return self.flashObject.as_setPaginatorData(pages)

    def as_setPageDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPageData(data)