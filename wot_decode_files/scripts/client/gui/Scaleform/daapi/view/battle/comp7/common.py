# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/common.py
from account_helpers import AccountSettings
from account_helpers.AccountSettings import COMP7_PREBATTLE_CAROUSEL_ROW_VALUE

def getSavedRowCountValue():
    savedRowCount = AccountSettings.getSettings(COMP7_PREBATTLE_CAROUSEL_ROW_VALUE)
    return (
     savedRowCount, savedRowCount != -1)


def rowValueToRowCount(rowValue):
    return rowValue + 1


def rowCountToRowValue(rowCount):
    return rowCount - 1