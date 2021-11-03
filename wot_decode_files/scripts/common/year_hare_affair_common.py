# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/year_hare_affair_common.py
SERVER_SETTINGS_KEY = 'year_hare_affair_config'
YHA_FINAL_QUEST_ID = 'YHA_COMMON'

def isYearHareAffairFinalTokenQuest(questID):
    return questID == YHA_FINAL_QUEST_ID