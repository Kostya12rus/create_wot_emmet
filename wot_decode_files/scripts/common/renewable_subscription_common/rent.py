# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/renewable_subscription_common/rent.py
from enum import Enum

class RentEventTypes(Enum):
    START_RENT = 1
    END_RENT = 2


class RentLogInfo(Enum):
    ADD = 'excl_veh:add'
    START = 'excl_veh:on'
    END = 'excl_veh:off'