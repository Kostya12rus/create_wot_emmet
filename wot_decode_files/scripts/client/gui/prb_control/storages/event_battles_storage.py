# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/event_battles_storage.py
from gui.battle_control.arena_visitor import createByAvatar
from gui.prb_control.storages.selection_storage import SelectionStorage
from helpers import dependency
from skeletons.gui.server_events import IEventsCache

class EventBattlesStorage(SelectionStorage):
    eventsCache = dependency.descriptor(IEventsCache)

    def isModeSelected(self):
        return self._isSelected and self.eventsCache.isEventEnabled()

    def _isInMode(self):
        arenaVisitor = createByAvatar()
        return arenaVisitor.gui.isEventBattle()