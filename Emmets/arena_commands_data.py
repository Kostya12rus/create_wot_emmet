# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/arena_commands_data.py
from collections import namedtuple
HESH_MAP_SIZE = 1000
HESH_GRID_STEP = 6
MAX_POSE_SIZE = HESH_MAP_SIZE / HESH_GRID_STEP

def getHashCode(pose):
    return sum([ int(coord + HESH_MAP_SIZE * 0.5 + 0.5) / HESH_GRID_STEP * MAX_POSE_SIZE ** i for i, coord in enumerate(pose)
               ])


class ArenaCommandData(namedtuple('ArenaCommandData', [
 'commandName', 
 'position', 
 'owner', 
 'name', 
 'state'])):

    @staticmethod
    def getCommandData(*args, **kwargs):
        if kwargs:
            data = ArenaCommandData(kwargs.get('commandName', 'PREBATTLE_WAYPOINT'), kwargs.get('position', (0.0,
                                                                                                             0.0,
                                                                                                             0.0)), kwargs.get('team', '') or kwargs.get('teams', 'both'), kwargs.get('name', '') or kwargs.get('locationName', 'ERROR'), kwargs.get('state', 'IDLE'))
            return (
             getHashCode(kwargs['position']), data)
        else:
            return


ArenaCommandData.__new__.__defaults__ = (None, ) * len(ArenaCommandData._fields)