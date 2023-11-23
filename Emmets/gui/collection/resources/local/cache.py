# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/collection/resources/local/cache.py
import typing
from gui.collection import loggers
from gui.impl import backport
from gui.impl.gen import R
_logger = loggers.getLocalCacheLogger()
if typing.TYPE_CHECKING:
    from typing import Dict, List

class CollectionsLocalCacheMgr(object):
    __IMG = R.images.gui.maps.icons.collections.fakeCdn.images

    def startSync(self, *args, **kwargs):
        _logger.debug('Sync started')

    def stopSync(self, *args, **kwargs):
        _logger.debug('Sync stopped')

    def getImagesPaths(self, imagesIDs, callback=None):
        callback(True, self.__packImages(imagesIDs))

    def __packImages(self, imagesIDs):
        packed = {}
        for imageID in imagesIDs:
            group, sub, name = imageID.split('/')
            packed.setdefault(group, {})
            packed[group].setdefault(sub, {})
            res = self.__IMG.dyn(group).dyn(sub).dyn(name)
            if res.exists():
                packed[group][sub][name] = backport.image(res())

        return packed