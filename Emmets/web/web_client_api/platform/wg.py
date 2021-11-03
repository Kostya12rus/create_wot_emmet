# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/platform/wg.py
from constants import DISTRIBUTION_PLATFORM
from web.web_client_api.platform.base import IPlatformWebApi

class WgPlatformWebApi(IPlatformWebApi):

    def getType(self):
        return DISTRIBUTION_PLATFORM.WG.value

    def isInited(self):
        return True

    def isConnected(self):
        return True