# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/collections/constants.py
from enum import Enum
FEATURE = 'collection'

class CollectionsItem(Enum):
    REWARD_NOTIFICATION = 'reward_notification'
    GAME_OBJECT = 'game_object'