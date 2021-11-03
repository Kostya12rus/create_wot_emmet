# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/core/common.py
import logging, typing
from gui.shared.utils import getPlayerDatabaseID
from helpers import getClientVersion
_logger = logging.getLogger(__name__)
_CLIENT_VERSION = None

def createFeatureKey(feature, group):
    return feature


def getPlayerID():
    playerID = getPlayerDatabaseID()
    if not playerID:
        _logger.warning('Player id not available or player is bot.')
        return
    return playerID


def getClientBuildVersion():
    global _CLIENT_VERSION
    if _CLIENT_VERSION is None:
        _CLIENT_VERSION = getClientVersion()
    return _CLIENT_VERSION