# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/hubs/dev/gifter.py
import logging
from adisp import adisp_process
from gui.gift_system.constants import GifterResponseState
from gui.gift_system.hubs.base.gifter import GiftEventBaseGifter
from gui.gift_system.hubs.dev import IDevMessagesPusher
from gui.shared.formatters import text_styles
_logger = logging.getLogger(__name__)

class GiftEventDevGifter(GiftEventBaseGifter, IDevMessagesPusher):
    __slots__ = ()

    def __repr__(self):
        return ('GiftEventDevGifter id={}').format(self._settings.eventID)

    @adisp_process
    def sendGift(self, entitlementCode, receiverID, metaInfo, callback=None):
        result = yield super(GiftEventDevGifter, self).sendGift(entitlementCode, receiverID, metaInfo)
        if result.state not in (GifterResponseState.WEB_SUCCESS, GifterResponseState.WEB_FAILURE):
            _logger.info('%s send gift rejected by reason=%s', self, result.state.value)
            self._pushClientMessage(('{}\nsend gift rejected').format(self))

    @classmethod
    def _formatMessage(cls, message):
        return text_styles.statusAlert(message)