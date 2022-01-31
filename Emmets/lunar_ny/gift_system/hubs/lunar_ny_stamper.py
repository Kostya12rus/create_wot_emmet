# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/lunar_ny/gift_system/hubs/lunar_ny_stamper.py
from itertools import chain
from gui.gift_system.hubs.base.stamper import GiftEventBaseStamper
from lunar_ny.lunar_ny_constants import ENVELOPE_ENTITLEMENT_CODE_TO_TYPE, ENVELOPE_IN_SECRET_SANTA_ENTITLEMENTS

class GiftLunarNYStamper(GiftEventBaseStamper):
    __slots__ = ()
    _STAMPS = set(chain.from_iterable([
     ENVELOPE_ENTITLEMENT_CODE_TO_TYPE.keys(), ENVELOPE_IN_SECRET_SANTA_ENTITLEMENTS.values()]))