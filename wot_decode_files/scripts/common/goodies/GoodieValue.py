# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/goodies/GoodieValue.py
from soft_exception import SoftException
from math import floor

class GoodieValue(object):
    __slots__ = [
     'value', 'isAbsolute']

    def __init__(self, value, isAbsolute=True):
        self.isAbsolute = isAbsolute
        if isAbsolute:
            self.value = int(value)
        else:
            if value < 0:
                raise SoftException('Bad goodie value <%s>' % value)
            self.value = float(value) / 100

    def __lt__(self, other):
        if self.isAbsolute == other.isAbsolute:
            return self.value < other.value
        raise SoftException('Comparison of absolute and percent values')

    def __gt__(self, other):
        if self.isAbsolute == other.isAbsolute:
            return self.value > other.value
        raise SoftException('Comparison of absolute and percent values')

    def __eq__(self, other):
        if self.isAbsolute == other.isAbsolute:
            return self.value == other.value
        raise SoftException('Comparison of absolute and percent values')

    @staticmethod
    def percent(value):
        return GoodieValue(value, False)

    @staticmethod
    def absolute(value):
        return GoodieValue(value, True)

    def increase(self, x):
        if self.isAbsolute:
            return int(x) + self.value
        else:
            return int(floor(x + float(x) * self.value))

    def reduce(self, x):
        if self.isAbsolute:
            result = int(x) - self.value
            if result < 0:
                raise SoftException('Goodie is negative %d > %d' % (self.value, x))
            return result
        return int(floor(x - float(x) * self.value))

    def delta(self, x):
        if self.isAbsolute:
            return self.value
        else:
            return int(round(float(x) * self.value))