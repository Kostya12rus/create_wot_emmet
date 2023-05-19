# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/epic_storage.py
from gui.prb_control.storages.local_storage import SessionStorage, ARENA_GUI_TYPE

class EpicStorage(SessionStorage):
    _GUI_TYPE = ARENA_GUI_TYPE.EPIC_BATTLE