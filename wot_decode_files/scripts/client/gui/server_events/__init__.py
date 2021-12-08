# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/__init__.py
from gui.server_events.EventsCache import EventsCache as _EventsCache
from gui.server_events.linkedset_controller import LinkedSetController as _LinkedSetController
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.linkedset import ILinkedSetController
__all__ = ('getServerEventsConfig', 'getLinkedSetController')

def getServerEventsConfig(manager):
    cache = _EventsCache()
    cache.init()
    manager.addInstance(IEventsCache, cache, finalizer='fini')


def getLinkedSetController(manager):
    controller = _LinkedSetController()
    controller.init()
    manager.addInstance(ILinkedSetController, controller, finalizer='fini')