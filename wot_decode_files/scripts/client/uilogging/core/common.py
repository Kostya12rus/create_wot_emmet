# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/core/common.py
import typing
from enum import Enum
from itertools import izip_longest
from helpers import getClientVersion

def getClientBuildVersion():
    return getClientVersion(force=False)


def grouper(iterable, batch):
    args = [
     iter(iterable)] * batch
    for parts in izip_longest(fillvalue=None, *args):
        yield [ part for part in parts if part is not None ]

    return


def convertEnum(value):
    if isinstance(value, Enum):
        return value.value
    return value