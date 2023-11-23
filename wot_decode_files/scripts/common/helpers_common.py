# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/helpers_common.py
from typing import Sequence
from soft_exception import SoftException

def bisectLE(a, v, lo=0, hi=None):
    if lo < 0:
        raise SoftException('lo must be non-negative')
    if hi is None:
        hi = len(a) - 1
    while lo < hi:
        mid = (lo + hi >> 1) + 1
        if a[mid] <= v:
            lo = mid
        else:
            hi = mid - 1

    return lo