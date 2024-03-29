# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rally/BaseRallyListView.py
from abc import abstractmethod
from gui import makeHtmlString
from gui.Scaleform.daapi.view.meta.BaseRallyListViewMeta import BaseRallyListViewMeta
from messenger.proto.events import g_messengerEvents

class BaseRallyListView(BaseRallyListViewMeta):

    def __init__(self):
        super(BaseRallyListView, self).__init__()
        self._searchDP = None
        return

    @abstractmethod
    def getPyDataProvider(self):
        return

    def setData(self, initialData):
        pass

    def _populate(self):
        super(BaseRallyListView, self)._populate()
        g_messengerEvents.users.onUserActionReceived += self._onUserActionReceived
        self._searchDP = self.getPyDataProvider()
        if self._searchDP:
            self._searchDP.setFlashObject(self.as_getSearchDPS())

    def _dispose(self):
        if self._searchDP is not None:
            self._searchDP.fini()
            self._searchDP = None
        g_messengerEvents.users.onUserActionReceived -= self._onUserActionReceived
        super(BaseRallyListView, self)._dispose()
        return

    def getRallyDetails(self, index):
        _, vo = self._searchDP.getRally(index)
        return vo

    def _updateVehiclesLabel(self, minVal, maxVal):
        self.as_setVehiclesTitleS(makeHtmlString('html_templates:lobby/rally/', 'vehiclesLabel', {'minValue': minVal, 'maxValue': maxVal}))

    def _onUserActionReceived(self, _, user, shadowMode):
        pass