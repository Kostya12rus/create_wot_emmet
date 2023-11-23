# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/queues/LRUCache.py
import collections

class LRUCache(object):

    def __init__(self, limit):
        self.__cache = collections.OrderedDict()
        self.__limit = limit

    def get(self, key):
        try:
            value = self.__cache.pop(key)
            self.__cache[key] = value
            return value
        except KeyError:
            return

        return

    def peek(self, key):
        return self.__cache.get(key, None)

    def set(self, key, value):
        try:
            self.__cache.pop(key)
        except KeyError:
            if len(self.__cache) >= self.__limit:
                self.__cache.popitem(last=False)

        self.__cache[key] = value

    def pop(self, key):
        return self.__cache.pop(key, None)

    def clear(self):
        self.__cache.clear()