# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/seniority_awards.py
import logging
from gui.impl import backport
from helpers import dependency, time_utils
from skeletons.gui.lobby_context import ILobbyContext
from helpers.time_utils import getServerUTCTime
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getSeniorityAwardsAutoOpenDate(lobbyContext=None):
    config = lobbyContext.getServerSettings().getSeniorityAwardsConfig()
    autoOpenTime = config.autoOpenTimestamp()
    autoOpenLocalTime = time_utils.makeLocalServerTime(autoOpenTime)
    return backport.getLongDateFormat(autoOpenLocalTime)


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def autoOpenTimeExpired(lobbyContext=None):
    config = lobbyContext.getServerSettings().getSeniorityAwardsConfig()
    autoOpenTime = config.autoOpenTimestamp()
    return autoOpenTime < getServerUTCTime()