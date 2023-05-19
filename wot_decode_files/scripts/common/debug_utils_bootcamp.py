# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/debug_utils_bootcamp.py
from debug_utils import _doLog, _LogWrapper
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_TAGS, LOG_LEVEL

@_LogWrapper(LOG_LEVEL.SVR_RELEASE)
def LOG_DEBUG_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('DEBUG', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.DEV)
def LOG_DEBUG_DEV_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('DEBUG', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_NOTE_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('NOTE', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_WARNING_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('WARNING', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_ERROR_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('ERROR', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_CODEPOINT_WARNING_BOOTCAMP(*kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('WARNING', 'this code point should have never been reached', kargs, kwargs)


def LOG_CURRENT_EXCEPTION_BOOTCAMP():
    LOG_CURRENT_EXCEPTION(tags=[LOG_TAGS.BOOTCAMP], frame=2)


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_STATISTIC(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.STATISTIC)
    _doLog('DEBUG', msg, kargs, kwargs)