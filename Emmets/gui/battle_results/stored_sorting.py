# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/stored_sorting.py
from account_helpers import AccountSettings
from account_helpers.AccountSettings import STATS_REGULAR_SORTING
from account_helpers.AccountSettings import STATS_SORTIE_SORTING
from account_helpers.AccountSettings import STATS_COMP7_SORTING
from soft_exception import SoftException
from constants import ARENA_BONUS_TYPE
__all__ = ('STATS_REGULAR_SORTING', 'STATS_SORTIE_SORTING', 'STATS_COMP7_SORTING',
           'writeStatsSorting', 'readStatsSorting')
AVAILABLE_STATS_SORTINGS = [
 STATS_REGULAR_SORTING,
 STATS_SORTIE_SORTING,
 STATS_COMP7_SORTING]

def writeStatsSorting(bonusType, iconType, sortDirection):
    key = STATS_REGULAR_SORTING
    if bonusType == ARENA_BONUS_TYPE.COMP7:
        key = STATS_COMP7_SORTING
    value = {'iconType': iconType, 
       'sortDirection': sortDirection}
    AccountSettings.setSettings(key, value)


def readStatsSorting(key):
    if key not in AVAILABLE_STATS_SORTINGS:
        raise SoftException(('Sorting key {} is invalid').format(key))
    settings = AccountSettings.getSettings(key)
    return (
     settings.get('iconType'), settings.get('sortDirection'))