# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/proxy.py
import logging
from gifts.gifts_common import GiftEventID
from gui.gift_system.wrappers import IncomeSysMessage
from helpers import dependency
from messenger.formatters.service_channel import ServiceChannelFormatter
from shared_utils import makeTupleByDict
from skeletons.gui.game_control import IGiftSystemController
_logger = logging.getLogger(__name__)

class GiftSystemMessagesProxy(ServiceChannelFormatter):
    __giftSystemCtrl = dependency.descriptor(IGiftSystemController)

    def format(self, message, *args):
        messageData = message.data
        if not messageData or not isinstance(messageData, dict):
            _logger.error('GiftSystemMessagesProxy received unsupported message data=%s', messageData)
            return []
        else:
            eventID = messageData.get('eventID', GiftEventID.UNKNOWN)
            eventHub = self.__giftSystemCtrl.getEventHub(eventID)
            if eventHub is not None:
                try:
                    eventHub.processMessage(makeTupleByDict(IncomeSysMessage, messageData))
                except TypeError:
                    _logger.exception('GiftSystemMessagesProxy received message with incomplete data for IncomeSysMessage')

            else:
                _logger.warning('GiftSystemMessagesProxy received message for non-existent eventID=%s', eventID)
            return []