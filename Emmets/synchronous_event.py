# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/synchronous_event.py
from async import async, forwardAsFuture, await
from debug_utils import LOG_CURRENT_EXCEPTION
from Event import Event

class SynchronousEvent(Event):
    __slots__ = ()

    def __init__(self, manager=None):
        super(SynchronousEvent, self).__init__(manager)

    @async
    def __call__(self, *args, **kwargs):
        for delegate in self[:]:
            try:
                yield await(forwardAsFuture(delegate(*args, **kwargs)))
            except:
                LOG_CURRENT_EXCEPTION()