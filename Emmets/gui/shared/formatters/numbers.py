# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/numbers.py
from typing import Optional, Callable
from gui.impl import backport

def formatInt(value, negativeOrZero=None, formatter=backport.getIntegralFormat):
    if value <= 0 and negativeOrZero is not None:
        result = negativeOrZero
    else:
        result = formatter(value)
    return result


def makeStringWithThousandSymbol(value, digitLimit=4, formatter=backport.getIntegralFormat, defaultFormatter=None):
    limitValue = 10 ** digitLimit - 1
    if value > limitValue:
        result = formatter(int(value * 0.001)) + 'K'
    elif defaultFormatter is not None:
        result = defaultFormatter(value)
    else:
        result = formatInt(value, '-', formatter)
    return result