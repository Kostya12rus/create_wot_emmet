# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/telecom_rentals_common.py
from enum import IntEnum
RENT_TOKEN_NAME = 'telecom_rent_token'
PARTNERSHIP_TOKEN_NAME = 'telecom_partnership_token'
PARTNERSHIP_BLOCKED_TOKEN_NAME = 'telecom_partnership_blocked_token'
ROSTER_EXPIRATION_TOKEN_NAME = 'telecom_roster_expiration_token'
TELECOM_RENTALS_CONFIG = 'telecom_rentals_config'
TELECOM_RENTALS_RENT_KEY = 'telecom'

class PartnershipState(IntEnum):
    NO_PARTNERSHIP = 0
    ACTIVE_PARTNERSHIP = 1
    BLOCKED_PARTNERSHIP = 2