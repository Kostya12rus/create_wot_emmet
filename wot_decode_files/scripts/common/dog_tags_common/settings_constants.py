# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dog_tags_common/settings_constants.py
from enum import Enum
DT_PDATA_KEY = 'dogTags'

class Settings(Enum):
    SHOW_VICTIMS_DT = 'showVictimsDogTag'
    SHOW_DT_TO_KILLER = 'showDogTagToKiller'

    def __lt__(self, other):
        return self.value < other.value


SETTINGS_POSITIONS = {Settings.SHOW_VICTIMS_DT: 1, 
   Settings.SHOW_DT_TO_KILLER: 2}