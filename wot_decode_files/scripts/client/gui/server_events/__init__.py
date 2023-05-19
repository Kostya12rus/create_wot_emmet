# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/__init__.py
from gui.server_events.EventsCache import EventsCache as _EventsCache
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.battle_matters import IBattleMattersController
__all__ = ('getServerEventsConfig', 'getBattleMattersController')

def getServerEventsConfig(manager):
    cache = _EventsCache()
    cache.init()
    manager.addInstance(IEventsCache, cache, finalizer='fini')


def getBattleMattersController(manager):
    from gui.game_control.battle_matters_controller import BattleMattersController
    controller = BattleMattersController()
    controller.init()
    manager.addInstance(IBattleMattersController, controller, finalizer='fini')