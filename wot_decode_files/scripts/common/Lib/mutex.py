# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/mutex.py
from warnings import warnpy3k
warnpy3k('the mutex module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
from collections import deque

class mutex:

    def __init__(self):
        self.locked = False
        self.queue = deque()

    def test(self):
        return self.locked

    def testandset(self):
        if not self.locked:
            self.locked = True
            return True
        else:
            return False

    def lock(self, function, argument):
        if self.testandset():
            function(argument)
        else:
            self.queue.append((function, argument))

    def unlock(self):
        if self.queue:
            function, argument = self.queue.popleft()
            function(argument)
        else:
            self.locked = False