# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/clan_helpers.py
from constants import ClansConfig
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getClanQuestURL(lobbyContext=None):
    return lobbyContext.getServerSettings().getClansConfig().get(ClansConfig.QUEST_URL)


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getCraftMachineURL(lobbyContext=None):
    return lobbyContext.getServerSettings().getClansConfig().get(ClansConfig.CRAFT_MACHINE_URL)