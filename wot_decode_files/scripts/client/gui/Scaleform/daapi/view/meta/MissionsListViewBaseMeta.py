# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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