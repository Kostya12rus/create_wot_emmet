# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/performance/critical/constants.py
from enum import Enum

class Features(str, Enum):
    MEMORY_CRITICAL = 'memory_critical'


class Groups(str, Enum):
    EVENT = 'event'


class LogActions(str, Enum):
    MEMORY_CRITICAL_EVENT = 'memory_critical_event'