# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/new_year/craft/components/data_nodes/abstract_data_node.py
import Event

class IAbstractDataNode(object):

    def __init__(self):
        self.__onDataChangedEvent = Event.Event()
        self.__layerID = None
        self._nodesHolder = None
        return

    def init(self, parentNodesHolder, layerID):
        self._nodesHolder = parentNodesHolder
        self.__layerID = layerID
        self._onInit()

    def destroy(self):
        self.__onDataChangedEvent.clear()
        self.__layerID = None
        if self._nodesHolder is not None:
            self._onDestroy()
            self._nodesHolder = None
        return

    def addListener(self, delegate):
        self.__onDataChangedEvent += delegate

    def removeListener(self, delegate):
        self.__onDataChangedEvent -= delegate

    def updateData(self):
        raise NotImplementedError

    def updateCrafting(self, isInProgress=False):
        pass

    def _raiseOnDataChanged(self):
        self.__onDataChangedEvent(self.__layerID)

    def _onInit(self):
        raise NotImplementedError

    def _onDestroy(self):
        raise NotImplementedError