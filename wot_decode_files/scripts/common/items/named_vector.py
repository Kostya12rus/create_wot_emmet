# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/named_vector.py
from collections import defaultdict
__all__ = ('NamedVector', )

class NamedVector(defaultdict):

    def __init__(self, default_factory=int, args=None):
        super(NamedVector, self).__init__(default_factory, args or [])

    def __add__(self, other):
        r = NamedVector(self.default_factory, self.iteritems())
        r += other
        return r

    def __iadd__(self, other):
        for k, v in other.iteritems():
            self[k] += v

        return self

    __radd__ = __add__

    def __sub__(self, other):
        r = NamedVector(self.default_factory, self.iteritems())
        r -= other
        return r

    def __isub__(self, other):
        for k, v in other.iteritems():
            self[k] -= v

        return self

    __rsub__ = __sub__