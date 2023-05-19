# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/__init__.py
from gui.shared.utils.functions import getArenaGeometryName
from helpers.i18n import makeString
MAX_MEMBERS_IN_CLAN = 100

def getI18ArenaById(arenaId):
    return makeString('#arenas:%s/name' % getArenaGeometryName(arenaId))