# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseRallyListViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyView import BaseRallyView

class BaseRallyListViewMeta(BaseRallyView):

    def getRallyDetails(self, index):
        self._printOverrideError('getRallyDetails')

    def as_selectByIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectByIndex(index)

    def as_selectByIDS(self, rallyID):
        if self._isDAAPIInited():
            return self.flashObject.as_selectByID(rallyID)

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_setDetailsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDetails(value)

    def as_setVehiclesTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesTitle(value)