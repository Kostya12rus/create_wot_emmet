# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/hubs/dev/stamper.py
import logging
from gui.gift_system.constants import DEV_STAMP_CODE
from gui.gift_system.hubs.base.stamper import GiftEventBaseStamper
_logger = logging.getLogger(__name__)

class GiftEventDevStamper(GiftEventBaseStamper):
    __slots__ = ()
    _STAMPS = {
     DEV_STAMP_CODE}