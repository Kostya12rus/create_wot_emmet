# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/subscriptions.py
from gui.clans.interfaces import IClanListener
from gui.shared.utils.listeners_collection import ListenersCollection

class WebListeners(ListenersCollection):

    def __init__(self):
        super(WebListeners, self).__init__()
        self._setListenerClass(IClanListener)

    def notify(self, eventType, *args):
        self._invokeListeners(eventType, *args)

    def addListener(self, listener):
        if not self.hasListener(listener):
            super(WebListeners, self).addListener(listener)

    def getListenersIterator(self):
        return list(super(WebListeners, self).getListenersIterator())