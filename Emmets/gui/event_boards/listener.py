# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/event_boards/listener.py
from gui.shared.utils.listeners_collection import ListenersCollection

class IEventBoardsListener(ListenersCollection):

    def __init__(self):
        super(IEventBoardsListener, self).__init__()
        self._setListenerClass(IEventBoardsListener)

    def onUpdateHangarFlag(self):
        pass