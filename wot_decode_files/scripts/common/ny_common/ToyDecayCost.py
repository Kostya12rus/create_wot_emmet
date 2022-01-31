# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/ny_common/ToyDecayCost.py
from typing import Optional, TYPE_CHECKING
from items import new_year
if TYPE_CHECKING:
    from items.collectibles import ToyDescriptor

class ToyDecayCostConfig(object):
    __slots__ = ('_config', )

    def __init__(self, config):
        self._config = config

    def getToyDecayCost(self, toyID=None, toyDescr=None):
        if toyDescr is None:
            toyDescr = new_year.g_cache.toys[toyID]
        return getattr(toyDescr, 'fragments', 0) or self._config.get((toyDescr.type, toyDescr.rank), 0)