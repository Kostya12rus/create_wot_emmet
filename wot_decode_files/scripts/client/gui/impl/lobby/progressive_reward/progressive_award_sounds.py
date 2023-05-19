# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/progressive_reward/progressive_award_sounds.py
import WWISE
from shared_utils import CONST_CONTAINER

class ProgressiveRewardSoundEvents(CONST_CONTAINER):
    PROGRESSIVE_REWARD_VIEW_GROUP = 'STATE_overlay_hangar_general'
    PROGRESSIVE_REWARD_VIEW_ENTER = 'STATE_overlay_hangar_general_on'
    PROGRESSIVE_REWARD_VIEW_EXIT = 'STATE_overlay_hangar_general_off'
    PROGRESSIVE_REWARD_AWARD_GROUP = 'STATE_overlay_hangar_general'
    PROGRESSIVE_REWARD_AWARD_ENTER = 'STATE_overlay_hangar_general_on'
    PROGRESSIVE_REWARD_AWARD_EXIT = 'STATE_overlay_hangar_general_off'


def setSoundState(groupName, stateName, eventName=None):
    playSound(eventName=eventName)
    WWISE.WW_setState(groupName, stateName)


def playSound(eventName):
    if eventName:
        WWISE.WW_eventGlobal(eventName)