# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/hubs/__init__.py
import typing
from gifts.gifts_common import GiftEventID
from gui.gift_system.hubs.base.hub_core import GiftEventBaseHub
from gui.gift_system.hubs.dev.hub_core import GiftEventDevHub
if typing.TYPE_CHECKING:
    from gui.gift_system.hubs.base.hub_core import IGiftEventHub
    from helpers.server_settings import GiftEventConfig
_HUB_BY_EVENT_ID = {GiftEventID.DEV_TEST: GiftEventDevHub}

def createGiftEventHub(eventID, eventSettings, isMessagesAllowed):
    return _HUB_BY_EVENT_ID.get(eventID, GiftEventBaseHub)(eventSettings, isMessagesAllowed)