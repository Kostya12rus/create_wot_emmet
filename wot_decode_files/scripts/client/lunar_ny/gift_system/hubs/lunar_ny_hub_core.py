# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/lunar_ny/gift_system/hubs/lunar_ny_hub_core.py
import typing
from gui.gift_system.hubs import GiftEventBaseHub
from gui.gift_system.hubs.dev import IDevMessagesPusher
from lunar_ny.gift_system.hubs.lunar_ny_gifter import LunarNYGifter
from lunar_ny.gift_system.hubs.lunar_ny_messenger import GiftLunarNYMessenger
from lunar_ny.gift_system.hubs.lunar_ny_stamper import GiftLunarNYStamper
from lunar_ny.gift_system.hubs.lunar_ny_keeper import GiftLunarNYKeeper
if typing.TYPE_CHECKING:
    from helpers.server_settings import GiftEventConfig

class GiftLunarNYHub(GiftEventBaseHub, IDevMessagesPusher):

    def _createStamper(self, eventSettings):
        return GiftLunarNYStamper(eventSettings, self._onStamperUpdate)

    def _createMessenger(self, eventSettings, isMessagesAllowed):
        return GiftLunarNYMessenger(eventSettings, isMessagesAllowed)

    def _createKeeper(self, eventSettings):
        return GiftLunarNYKeeper(eventSettings, self._onKeeperCleared)

    def _createGifter(self, eventSettings):
        return LunarNYGifter(eventSettings, self._onGifterResponse)