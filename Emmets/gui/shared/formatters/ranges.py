# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/ranges.py
from helpers import int2roman

def toRangeString(sequence, step=1, itemDelimiter=', ', rangeDelimiter='-'):
    items = list()
    for item in list(stringRanges(sequence, step)):
        items.append(rangeDelimiter.join(item))

    return itemDelimiter.join(items)


def toRomanRangeString(sequence, step=1, itemDelimiter=', ', rangeDelimiter='-'):
    items = list()
    for item in list(romanStringRanges(sequence, step)):
        items.append(rangeDelimiter.join(item))

    return itemDelimiter.join(items)


def stringRanges(sequence, step):
    for item in numberRanges(sequence, step):
        yield map(str, item)


def romanStringRanges(sequence, step):
    for item in numberRanges(sequence, step):
        yield map(int2roman, item)


def numberRanges(sequence, step):
    length = len(sequence)
    if length > 0:
        q = sorted(sequence)
        i = 0
        for j in xrange(1, length):
            if q[j] > step + q[j - 1]:
                if i == j - 1:
                    yield (
                     q[i],)
                else:
                    yield (
                     q[i], q[j - 1])
                i = j

        if i == length - 1:
            yield (
             q[i],)
        else:
            yield (
             q[i], q[-1])