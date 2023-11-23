# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/collection/resources/common.py
import logging
from gui.collection.resources.cdn.cache import CollectionsCdnCacheMgr
from gui.collection.resources.local.cache import CollectionsLocalCacheMgr
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def makeCacheMgr(lobbyContext=None):
    settings = lobbyContext.getServerSettings()
    if settings.collectionsConfig.useCdnResourceCache:
        if settings.fileServer.getCollectionsContentConfigUrl():
            return CollectionsCdnCacheMgr()
        _logger.warning('External url not configured yet. The local cache will be used.')
    return CollectionsLocalCacheMgr()