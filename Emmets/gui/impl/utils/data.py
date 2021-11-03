# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/utils/data.py
import typing
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array
T = typing.TypeVar('T')

def findIndexes(arr, predicate):
    return [ idx for idx, item in enumerate(arr) if predicate(item) ]


def findItems(arr, predicate):
    return [ item for item in arr if predicate(item) ]