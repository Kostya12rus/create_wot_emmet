# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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