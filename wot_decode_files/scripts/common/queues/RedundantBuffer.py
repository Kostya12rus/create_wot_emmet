# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/queues/RedundantBuffer.py
import collections
from itertools import chain

class RedundantBuffer(object):

    def __init__(self, redundancy, callback=None, limit=None):
        self.__cache = collections.deque()
        self.__redundancy = redundancy
        self.__callback = callback
        self.__limit = limit

    def __repr__(self):
        return str(self.__cache)

    def snapshot(self):
        return list(chain.from_iterable(self.__cache))

    def flush(self):
        if not self.__cache:
            result = []
        else:
            result = self.snapshot()
            self.__cache.appendleft([])
            if len(self.__cache) > self.__redundancy:
                self.__cache.pop()
        if self.__callback is not None:
            self.__callback(result)
        return result

    def fini(self):
        for i in range(0, self.__redundancy):
            self.flush()

    def add(self, value):
        if not self.__cache:
            self.__cache.appendleft([value])
            return
        else:
            if self.__limit is not None and len(self.__cache[0]) >= self.__limit:
                self.flush()
            self.__cache[0].append(value)
            return

    def clear(self):
        self.__cache.clear()