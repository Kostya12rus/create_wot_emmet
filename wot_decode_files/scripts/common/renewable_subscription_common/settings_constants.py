# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/renewable_subscription_common/settings_constants.py
from enum import Enum
RS_PDATA_KEY = 'renewableSub'
RS_ENABLED = 'isEnabled'
RS_EXPIRATION_TIME = 'expiry'
IDLE_CREW_XP_PDATA_KEY = 'idleCrewXP'
GOLD_RESERVE_GAINS_SECTION = 'goldReserveGainsPerBattleType'
IDLE_CREW_VEH_INV_ID = 'vehInvID'
LAST_XP_UPDATE_TIMESTAMP = 'lastXPUpdate'
PASSIVE_XP_CURRENCY = 'currency'
ISSUED_XP_CACHE = 'xpCache'
RENT_KEY = 'subscription'
PASSIVE_XP_ENTITLEMENT = 'subscription_passive_xp'
PASSIVE_XP_SECONDS = 'passive_xp_seconds'
SUBSCRIPTION_DURATION_LENGTH = 2592000
WOTPLUS_BADGE_ID = 106
DEFAULT_DEMOUNT_ACTION = 0
WOT_PLUS_DEMOUNT_ACTION = 1

class WotPlusState(Enum):
    INACTIVE = 0
    ACTIVE = 1
    CANCELLED = 2