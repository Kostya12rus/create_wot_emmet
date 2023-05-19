# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/resource_well/resource_well_constants.py
import logging
from enum import IntEnum, Enum
_logger = logging.getLogger(__name__)
RESOURCE_WELL_PDATA_KEY = 'resourceWell'
UNAVAILABLE_REWARD_ERROR = 'UNAVAILABLE_REWARD_ERROR'
CHANNEL_NAME_PREFIX = 'suv_'

class ProgressionState(IntEnum):
    ACTIVE = 1
    NO_PROGRESS = 2
    NO_VEHICLES = 3
    FORBIDDEN = 4


class ResourceType(Enum):
    BLUEPRINTS = 'blueprints'
    CURRENCY = 'currency'

    @classmethod
    def getMember(cls, value):
        if value in cls._value2member_map_:
            return cls(value)
        else:
            _logger.error('%s does not exist in ResourceType values', value)
            return