# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/platform/steam.py
from __future__ import absolute_import
import logging, Steam
from constants import DISTRIBUTION_PLATFORM
from web.web_client_api.platform.base import IPlatformWebApi
_logger = logging.getLogger(__name__)

class SteamPlatformWebApi(IPlatformWebApi):

    def getType(self):
        return DISTRIBUTION_PLATFORM.STEAM.value

    def isInited(self):
        return Steam.isInited()

    def isConnected(self):
        return Steam.isInited()