# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsListViewBaseMeta.py
from gui.Scaleform.daapi.view.meta.MissionsViewBaseMeta import MissionsViewBaseMeta

class MissionsListViewBaseMeta(MissionsViewBaseMeta):

    def openMissionDetailsView(self, id, blockId):
        self._printOverrideError('openMissionDetailsView')

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()

    def as_scrollToItemS(self, idFieldName, itemId):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToItem(idFieldName, itemId)