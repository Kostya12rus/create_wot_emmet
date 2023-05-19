# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/math_common.py
from math import ceil
_CEIL_EPS = 1

def ceilTo(num, decimals=0):
    multiplier = 10 ** decimals
    return ceil(round(num / multiplier, _CEIL_EPS)) * multiplier


def round_int(number):
    return int(round(number))


def isAlmostEqual(first, second, epsilon=0.0004):
    return second - epsilon <= first <= second + epsilon


def trim(v, min, max):
    if v < min:
        v = min
    elif v > max:
        v = max
    return v