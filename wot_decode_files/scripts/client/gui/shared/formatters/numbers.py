# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/numbers.py
from gui.impl import backport

def formatInt(value, negativeOrZero=None, formatter=backport.getIntegralFormat):
    if value <= 0 and negativeOrZero is not None:
        result = negativeOrZero
    else:
        result = formatter(value)
    return result


def makeStringWithThousandSymbol(value, digitLimit=4, formatter=backport.getIntegralFormat):
    limitValue = 10 ** digitLimit - 1
    if value > limitValue:
        result = formatter(int(value * 0.001)) + 'K'
    else:
        result = formatInt(value, '-', formatter)
    return result