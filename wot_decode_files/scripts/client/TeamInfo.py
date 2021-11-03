# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/TeamInfo.py
import BigWorld
from debug_utils import LOG_DEBUG_DEV

class TeamInfo(BigWorld.Entity):

    def __init__(self):
        LOG_DEBUG_DEV(('[TeamInfo] __init__: team = {}').format(self.teamID))

    def onEnterWorld(self, prereqs):
        LOG_DEBUG_DEV(('[TeamInfo] onEnterWorld: team = {}').format(self.teamID))
        BigWorld.player().arena.registerTeamInfo(self)

    def onLeaveWorld(self):
        LOG_DEBUG_DEV(('[TeamInfo] onLeaveWorld: team = {}').format(self.teamID))
        BigWorld.player().arena.unregisterTeamInfo(self)