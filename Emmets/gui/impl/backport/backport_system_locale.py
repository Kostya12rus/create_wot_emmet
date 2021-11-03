# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/backport/backport_system_locale.py
from frameworks import wulf

def getIntegralFormat(value):
    return wulf.getNumberFormat(value, wulf.NumberFormatType.INTEGRAL)


def getGoldFormat(value):
    return wulf.getNumberFormat(value, wulf.NumberFormatType.GOLD)


def getFractionalFormat(value):
    return wulf.getRealFormat(value, wulf.RealFormatType.FRACTIONAL)


def getNiceNumberFormat(value):
    return wulf.getRealFormat(value, wulf.RealFormatType.WO_ZERO_DIGITS)


def getShortTimeFormat(value):
    return wulf.getTimeFormat(value, wulf.TimeFormatType.SHORT_FORMAT)


def getLongTimeFormat(value):
    return wulf.getTimeFormat(value, wulf.TimeFormatType.LONG_FORMAT)


def getShortDateFormat(value):
    return wulf.getDateFormat(value, wulf.DateFormatType.SHORT_FORMAT)


def getLongDateFormat(value):
    return wulf.getDateFormat(value, wulf.DateFormatType.LONG_FORMAT)


def getYearMonthFormat(value):
    return wulf.getDateFormat(value, wulf.DateFormatType.YEAR_MONTH)


def getDateTimeFormat(value):
    return ('{0:>s} {1:>s}').format(wulf.getDateFormat(value, wulf.DateFormatType.LONG_FORMAT), wulf.getTimeFormat(value, wulf.TimeFormatType.SHORT_FORMAT))