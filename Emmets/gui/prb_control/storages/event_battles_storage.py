# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/event_battles_storage.py
from gui.prb_control.storages.local_storage import SessionStorage, ARENA_GUI_TYPE

class EventBattlesStorage(SessionStorage):
    _GUI_TYPE = ARENA_GUI_TYPE.EVENT_BATTLES