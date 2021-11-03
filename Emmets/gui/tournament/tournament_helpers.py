# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/tournament/tournament_helpers.py
from debug_utils import LOG_CURRENT_EXCEPTION
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from gui import GUI_SETTINGS

def getTournamentUrl(urlName=None):
    try:
        return _getTMSHost() + GUI_SETTINGS.tournament.get(urlName or 'testUrl')
    except (AttributeError, TypeError):
        LOG_CURRENT_EXCEPTION()
        return

    return


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def _getTMSHost(lobbyContext=None):
    if lobbyContext is None:
        return
    else:
        try:
            return lobbyContext.getServerSettings().tournament.tmsHostUrl
        except AttributeError:
            LOG_CURRENT_EXCEPTION()
            return

        return