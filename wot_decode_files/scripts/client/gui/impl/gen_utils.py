# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen_utils.py
from typing import Optional, Generator, Iterator
INVALID_RES_ID = -1

class DynAccessor(object):
    __slots__ = ('__resId', )

    def __init__(self, value=0):
        self.__resId = value

    def __call__(self):
        return self.__resId

    def __nonzero__(self):
        return self.__resId >= 0

    def dyn(self, attr, default=None):
        return getattr(self, attr, default or _g_invalid)

    def num(self, attr, default=None):
        return getattr(self, ('c_{}').format(attr), default or _g_invalid)

    def keys(self):
        return (attr for attr in dir(self) if attr not in dir(DynAccessor) and not attr.startswith('_'))

    def values(self):
        return (getattr(self, attr) for attr in self.keys())

    def items(self):
        return ((attr, getattr(self, attr)) for attr in self.keys())

    def length(self):
        return len(tuple(self.keys()))

    def exists(self):
        return self.__resId > 0

    def isValid(self):
        return True


class _InvalidDynAccessor(DynAccessor):

    def keys(self):
        return iter(())

    def isValid(self):
        return False


_g_invalid = _InvalidDynAccessor(INVALID_RES_ID)