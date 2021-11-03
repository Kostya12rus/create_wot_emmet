# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_maintenance.py
from gui.Scaleform.daapi.view.meta.MaintenanceComponentMeta import MaintenanceComponentMeta
import Event

class EventBoardsMaintenance(MaintenanceComponentMeta):

    def __init__(self):
        super(EventBoardsMaintenance, self).__init__()
        self.onRefresh = Event.Event()

    def refresh(self):
        self.onRefresh()