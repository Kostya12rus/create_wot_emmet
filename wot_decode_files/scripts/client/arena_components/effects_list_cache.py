# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/arena_components/effects_list_cache.py
from arena_component_system.client_arena_component_system import ClientArenaComponent
from helpers import EffectsList

class EffectsListCache(object):

    def __init__(self):
        self.__cache = {}

    def load(self, effectsListName, effectsListDataSection):
        effectsListTimeLine = self.__cache.get(effectsListName)
        if effectsListTimeLine is not None:
            return effectsListTimeLine
        else:
            effectsListTimeLine = EffectsList.effectsFromSection(effectsListDataSection)
            self.__cache[effectsListName] = effectsListTimeLine
            return effectsListTimeLine

    def loadFromRootDataSection(self, effectsListName, effectsListRootDataSection):
        return self.load(effectsListName, effectsListRootDataSection[effectsListName])


class EffectsListCacheComponent(ClientArenaComponent, EffectsListCache):

    def __init__(self, componentSystem):
        ClientArenaComponent.__init__(self, componentSystem)
        EffectsListCache.__init__(self)