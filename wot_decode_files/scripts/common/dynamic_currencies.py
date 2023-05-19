# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dynamic_currencies.py
from hashlib import md5
from typing import Dict

class DynamicCurrenciesData:

    def __init__(self):
        self.__currencies = {}
        self.__loaded = False

    def getData(self):
        return self.__currencies

    def setData(self, data):
        self.__currencies = data
        self.__loaded = True

    def replaceData(self, data):
        self.__currencies.update(data)

    @property
    def loaded(self):
        return self.__loaded

    def isCurrencyCodeCorrect(self, currencyCode):
        return not self.__loaded or currencyCode in self.__currencies


def getCurrencyCD(currencyCode):
    cd_hex = md5(currencyCode).hexdigest()[:7]
    return int(cd_hex, 16)


g_dynamicCurrenciesData = DynamicCurrenciesData()