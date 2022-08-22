# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/goodies/__init__.py
from gui.goodies.storage_novelty import StorageNovelty
from gui.goodies.goodies_cache import GoodiesCache
from skeletons.gui.storage_novelty import IStorageNovelty
from skeletons.gui.goodies import IGoodiesCache
__all__ = ('getGoodiesCacheConfig', 'getStorageNoveltyConfig')

def getGoodiesCacheConfig(manager):
    cache = GoodiesCache()
    cache.init()
    manager.addInstance(IGoodiesCache, cache, finalizer='fini')


def getStorageNoveltyConfig(manager):

    def _create():
        instance = StorageNovelty()
        instance.init()
        return instance

    manager.addRuntime(IStorageNovelty, _create, finalizer='fini')