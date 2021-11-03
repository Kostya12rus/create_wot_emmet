# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/ListPaginator.py
import weakref, Event

class ListPaginator(object):

    def __init__(self, requester, offset=None, count=20):
        super(ListPaginator, self).__init__()
        self._eManager = Event.EventManager()
        self.onListUpdated = Event.Event(self._eManager)
        if offset is not None:
            self.__initialOffset = offset
        else:
            self.__initialOffset = -count / 2
        self._offset = self.__initialOffset
        self._prevOffset = self._offset
        self._count = count
        self._selectedID = None
        self._requester = weakref.proxy(requester)
        return

    def init(self):
        pass

    def fini(self):
        self._eManager.clear()

    def canMoveLeft(self):
        return True

    def canMoveRight(self):
        return True

    def right(self):
        self._selectedID = None
        self._prevOffset = self._offset
        self._offset += self._count
        self._request()
        return

    def left(self):
        self._selectedID = None
        self._prevOffset = self._offset
        self._offset -= self._count
        self._request()
        return

    def reset(self):
        self._selectedID = None
        self._offset = self.__initialOffset
        self._prevOffset = self._offset
        self._request(isReset=True)
        return

    def getInitialOffset(self):
        return self.__initialOffset

    def revertOffset(self):
        self._offset = self._prevOffset

    def refresh(self, *args, **kwargs):
        self._request()

    def setSelectedID(self, selectedID):
        self._selectedID = selectedID

    def getSelectedID(self):
        return self._selectedID

    def _request(self, isReset=False):
        raise NotImplementedError