# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/events_debugger.py
from debug_utils import LOG_DEBUG_DEV

def _iterEventNames(events):
    return (name for name in dir(events) if name.startswith('on'))


class EventsDebugger(object):

    def __init__(self, events):
        for eventName in _iterEventNames(events):
            event = getattr(events, eventName)
            processor = getattr(self, eventName)
            event += processor

    def _shouldHandle(self, eventName):
        return True

    def _getDebugPrefix(self):
        return '[EVENT]'

    def _buildDebugString(self, item):
        return '%s %s' % (self._getDebugPrefix(), item)

    def __getattr__(self, item):
        if self._shouldHandle(item):
            return (lambda *args, **kwargs: LOG_DEBUG_DEV(self._buildDebugString(item), *args, **kwargs))
        else:
            return (lambda *args, **kwargs: None)