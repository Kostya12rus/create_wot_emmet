# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/avatars.py
from extension_utils import ResMgr
from items import _xml, common_extras
from constants import IS_CLIENT, IS_CELLAPP, ITEM_DEFS_PATH
g_cache = None

def init():
    global g_cache
    g_cache = Cache()


class Cache(object):

    def __init__(self):
        self.__commonConfig = None
        return

    @property
    def commonConfig(self):
        config = self.__commonConfig
        if config is None:
            configXmlPath = ITEM_DEFS_PATH + 'avatar.xml'
            configXml = ResMgr.openSection(configXmlPath)
            if configXml is None:
                _xml.raiseWrongXml(None, configXmlPath, 'can not open or read')
            if IS_CLIENT or IS_CELLAPP:
                extras, extrasDict = common_extras.readExtras((None, configXmlPath), configXml, 'extras', 'avatar_extras')
                config = self.__commonConfig = {'extras': extras, 'extrasDict': extrasDict}
            configXml = None
            ResMgr.purge(configXmlPath, True)
        return config