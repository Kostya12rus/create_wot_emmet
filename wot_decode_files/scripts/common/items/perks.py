# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/perks.py
from constants import ITEM_DEFS_PATH
from items.readers.perks_readers import readPerksCacheFromXML
from items.components.perks_components import PerksCashe
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
            self.__perks = PerksCashe()
            readPerksCacheFromXML(self.__perks, _PERK_XML_PATH)
        return

    @property
    def perks(self):
        if self.__perks is None:
            self.initPerks()
        return self.__perks