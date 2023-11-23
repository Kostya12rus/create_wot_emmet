# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/platform/steam.py
from __future__ import absolute_import
import logging, Steam
from helpers.platform.base import BasePublishPlatform
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Literal
_logger = logging.getLogger(__name__)

class SteamPublishPlatform(BasePublishPlatform):

    def init(self):
        super(SteamPublishPlatform, self).init()
        if self.isInited():
            Steam.microTxnAuthorizationResponse(self.__onMicroTxnAuthorizationResponse)
            Steam.gameOverlayActivated(self.__onGameOverlayActivated)
        else:
            _logger.error('Steam is not inited')

    def fini(self):
        Steam.microTxnAuthorizationResponse(None)
        Steam.gameOverlayActivated(None)
        super(SteamPublishPlatform, self).fini()
        return

    def isInited(self):
        return Steam.isInited()

    def isConnected(self):
        return Steam.isInited()

    def __onMicroTxnAuthorizationResponse(self, _, orderID, authorized):
        self.onPayment(orderID, authorized == 'true')

    def __onGameOverlayActivated(self, active):
        self.onOverlay(bool(active))