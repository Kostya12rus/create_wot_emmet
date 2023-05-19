# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/logger.py
from constants import IS_DEVELOPMENT
from debug_utils import _doLog, LOG_CURRENT_EXCEPTION

class LOG_LEVEL(object):
    ERROR = 1
    WARNING = 2
    DEBUG = 4
    MEMORY = 8
    REQUEST = 16


CURRENT_LOG_LEVEL = LOG_LEVEL.ERROR
if IS_DEVELOPMENT:
    CURRENT_LOG_LEVEL |= LOG_LEVEL.WARNING
    CURRENT_LOG_LEVEL |= LOG_LEVEL.REQUEST

def LOG_DEBUG(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.DEBUG:
        _doLog('TUTORIAL DEBUG', msg, args)


def LOG_WARNING(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.WARNING:
        _doLog('TUTORIAL WARNING', msg, args)


def LOG_ERROR(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.ERROR:
        _doLog('TUTORIAL ERROR', msg, args)


def LOG_MEMORY(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.MEMORY:
        _doLog('TUTORIAL MEMORY', msg, args)


def LOG_REQUEST(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.REQUEST:
        _doLog('TUTORIAL REQUEST', msg, args)


__all__ = ('LOG_DEBUG', 'LOG_WARNING', 'LOG_ERROR', 'LOG_MEMORY', 'LOG_REQUEST', 'LOG_CURRENT_EXCEPTION')