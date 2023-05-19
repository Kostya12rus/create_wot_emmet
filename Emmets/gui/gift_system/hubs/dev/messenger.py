# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/hubs/dev/messenger.py
import logging, typing
from gui.gift_system.hubs.base.messenger import GiftEventBaseMessenger
from gui.gift_system.hubs.dev import IDevMessagesPusher
from gui.shared.formatters import text_styles
if typing.TYPE_CHECKING:
    from gui.gift_system.wrappers import GiftsHistoryData, IncomeSysMessage, SendGiftResponse
_logger = logging.getLogger(__name__)

class GiftEventDevMessenger(GiftEventBaseMessenger, IDevMessagesPusher):
    __slots__ = ()

    def __repr__(self):
        return ('GiftEventDevMessenger id={}').format(self._settings.eventID)

    @classmethod
    def _formatMessage(cls, message):
        return text_styles.statInfo(message)

    def _pushHistoryMessage(self, history):
        _logger.info('%s push history message %s', self, history)
        self._pushClientMessage(('{}\npush history message').format(self))

    def _pushIncomeMessage(self, incomeData):
        _logger.info('%s push income message %s', self, incomeData)
        self._pushClientMessage(('{}\npush income message').format(self))

    def _pushOutcomeMessage(self, outcomeData):
        _logger.info('%s push outcome message %s', self, outcomeData)
        self._pushClientMessage(('{}\npush outcome message').format(self))