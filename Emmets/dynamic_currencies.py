# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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