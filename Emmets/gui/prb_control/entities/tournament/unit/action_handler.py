# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/tournament/unit/action_handler.py
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.entities.stronghold.unit.actions_handler import StrongholdActionsHandler

class TournamentActionsHandler(StrongholdActionsHandler):

    def showGUI(self):
        g_eventDispatcher.showTournamentWindow()