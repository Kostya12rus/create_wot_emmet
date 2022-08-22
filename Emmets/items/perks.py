# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/perks.py
from items.components.perks_components import PerksCache
from constants import ITEM_DEFS_PATH
from items.readers.perks_readers import readPerksCacheFromXML
_PERK_XML_PATH = ITEM_DEFS_PATH + 'perks/'
g_cache = None

def init(preloadEverything):
    global g_cache
    g_cache = Cache()
    if preloadEverything:
        g_cache.initPerks()


class Cache(object):
    __slots__ = '__perks'

    def __init__(self):
        self.__perks = None
        return

    def initPerks(self):
        if self.__perks is None:
            self.__perks = PerksCache()
            readPerksCacheFromXML(self.__perks, _PERK_XML_PATH)
        return

    def perks(self):
        if self.__perks is None:
            self.initPerks()
        return self.__perks