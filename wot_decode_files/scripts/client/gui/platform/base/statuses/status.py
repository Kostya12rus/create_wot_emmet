# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/base/statuses/status.py
import typing
from gui.platform.base.statuses.constants import StatusTypes

class Status(object):
    __slots__ = ('_type', '_data')

    def __init__(self, statusType=StatusTypes.UNDEFINED, data=None):
        self._type = statusType
        self._data = data or {}

    @property
    def data(self):
        return self._data

    @property
    def type(self):
        return self._type

    @property
    def isUndefined(self):
        return self.typeIs(StatusTypes.UNDEFINED)

    def typeIs(self, statusType):
        return self.type == statusType

    def __eq__(self, other):
        return (
         self.type, self.data) == (other.type, other.data)

    def __str__(self):
        return '<%s>: type=%s' % (self.__class__.__name__, self.type)

    def __repr__(self):
        return self.__str__()