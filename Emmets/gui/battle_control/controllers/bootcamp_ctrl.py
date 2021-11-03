# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/bootcamp_ctrl.py
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from helpers import dependency
from skeletons.gui.game_control import IGameSessionController
from bootcamp.BootCampEvents import g_bootcampEvents

class BootcampController(IArenaVehiclesController):
    gameSession = dependency.descriptor(IGameSessionController)

    def getControllerID(self):
        return

    def arenaLoadCompleted(self):
        g_bootcampEvents.onArenaLoadCompleted()