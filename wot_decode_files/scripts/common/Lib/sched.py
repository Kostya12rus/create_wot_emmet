# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/sched.py
import heapq
from collections import namedtuple
__all__ = [
 'scheduler']
Event = namedtuple('Event', 'time, priority, action, argument')

class scheduler:

    def __init__(self, timefunc, delayfunc):
        self._queue = []
        self.timefunc = timefunc
        self.delayfunc = delayfunc

    def enterabs(self, time, priority, action, argument):
        event = Event(time, priority, action, argument)
        heapq.heappush(self._queue, event)
        return event

    def enter(self, delay, priority, action, argument):
        time = self.timefunc() + delay
        return self.enterabs(time, priority, action, argument)

    def cancel(self, event):
        self._queue.remove(event)
        heapq.heapify(self._queue)

    def empty(self):
        return not self._queue

    def run(self):
        q = self._queue
        delayfunc = self.delayfunc
        timefunc = self.timefunc
        pop = heapq.heappop
        while q:
            time, priority, action, argument = checked_event = q[0]
            now = timefunc()
            if now < time:
                delayfunc(time - now)
            else:
                event = pop(q)
                if event is checked_event:
                    action(*argument)
                    delayfunc(0)
                else:
                    heapq.heappush(q, event)

    @property
    def queue(self):
        events = self._queue[:]
        return map(heapq.heappop, [events] * len(events))