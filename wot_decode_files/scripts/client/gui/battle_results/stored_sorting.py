# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/stored_sorting.py
from account_helpers import AccountSettings
from account_helpers.AccountSettings import STATS_REGULAR_SORTING
from account_helpers.AccountSettings import STATS_SORTIE_SORTING
from soft_exception import SoftException
__all__ = ('STATS_REGULAR_SORTING', 'STATS_SORTIE_SORTING', 'writeStatsSorting', 'readStatsSorting')

def writeStatsSorting(bonusType, iconType, sortDirection):
    key = STATS_REGULAR_SORTING
    value = {'iconType': iconType, 
       'sortDirection': sortDirection}
    AccountSettings.setSettings(key, value)


def readStatsSorting(key):
    if key not in (STATS_REGULAR_SORTING, STATS_SORTIE_SORTING):
        raise SoftException(('Sorting key {} is invalid').format(key))
    settings = AccountSettings.getSettings(key)
    return (
     settings.get('iconType'), settings.get('sortDirection'))