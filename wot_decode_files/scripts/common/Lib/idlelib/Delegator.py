# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/idlelib/Delegator.py


class Delegator:

    def __init__(self, delegate=None):
        self.delegate = delegate
        self.__cache = set()

    def __getattr__(self, name):
        attr = getattr(self.delegate, name)
        setattr(self, name, attr)
        self.__cache.add(name)
        return attr

    def resetcache(self):
        for key in self.__cache:
            try:
                delattr(self, key)
            except AttributeError:
                pass

        self.__cache.clear()

    def setdelegate(self, delegate):
        self.resetcache()
        self.delegate = delegate