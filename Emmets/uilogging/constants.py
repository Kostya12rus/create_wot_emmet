# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/constants.py
from enum import Enum
DEFAULT_LOGGER_NAME = 'UI_LOG'

class LogLevels(object):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30


class CommonLogActions(str, Enum):
    CLICK = 'click'
    KEYDOWN = 'keydown'