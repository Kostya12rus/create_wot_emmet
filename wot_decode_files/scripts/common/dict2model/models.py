# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dict2model/models.py
from __future__ import absolute_import
import typing
from itertools import chain

class Model(object):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(Model, self).__init__()

    def toDict(self):
        slots = set(chain.from_iterable(getattr(cls, '__slots__', tuple()) for cls in self.__class__.__mro__))
        return {attr: getattr(self, attr) for attr in slots if hasattr(self, attr)}