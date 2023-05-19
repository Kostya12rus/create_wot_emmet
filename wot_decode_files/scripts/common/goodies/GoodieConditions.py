# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/goodies/GoodieConditions.py


class Condition(object):

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def check(self, other):
        return self == other

    def __ne__(self, other):
        return not self.__eq__(other)


class MaxVehicleLevel(Condition):

    def __init__(self, level):
        self.level = level

    def __lt__(self, other):
        return self.level < other.level