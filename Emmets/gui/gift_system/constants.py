# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/constants.py
from enum import unique, Enum, IntEnum
DEV_STAMP_CODE = 'giftSystem_1_devStamp'

@unique
class GifterResponseState(Enum):
    WEB_FAILURE = 'webFailure'
    WEB_SUCCESS = 'webSuccess'
    REQUESTS_DISABLED = 'requestsDisabled'
    WGCG_NOT_AVAILABLE = 'wgcgNotAvailable'
    REQUEST_IN_PROGRESS = 'requestInProgress'
    CENTER_DISCONNECTED = 'centerDisconnected'


@unique
class GiftMessageType(IntEnum):
    INCOME = 0
    OUTCOME = 1
    HISTORY = 2
    LIMITS = 4


@unique
class HubUpdateReason(IntEnum):
    HISTORY = 0
    SETTINGS = 1
    WEB_STATE = 2
    INCOME_GIFT = 3
    OUTCOME_GIFT = 4
    KEEPER_CLEAR = 5
    STAMPER_UPDATE = 6