# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/goodies/__init__.py
from gui.goodies.booster_state_provider import BoosterStateProvider
from gui.goodies.storage_novelty import StorageNovelty
from gui.goodies.goodies_cache import GoodiesCache
from skeletons.gui.storage_novelty import IStorageNovelty
from skeletons.gui.goodies import IGoodiesCache, IBoostersStateProvider
from helpers.dependency import DependencyManager
__all__ = ('getGoodiesCacheConfig', 'getStorageNoveltyConfig')

def getGoodiesCacheConfig(manager):
    cache = GoodiesCache()
    cache.init()
    provider = BoosterStateProvider()
    manager.addInstance(IGoodiesCache, cache, finalizer='fini')
    manager.addInstance(IBoostersStateProvider, provider, finalizer='fini')


def getStorageNoveltyConfig(manager):

    def _create():
        instance = StorageNovelty()
        instance.init()
        return instance

    manager.addRuntime(IStorageNovelty, _create, finalizer='fini')