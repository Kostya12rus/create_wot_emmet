# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/seniority_awards/seniority_awards_sounds.py
import WWISE
from shared_utils import CONST_CONTAINER

class LootBoxViewEvents(CONST_CONTAINER):
    ENTRY_VIEW_ENTER = 'gui_lootbox_logistic_center_ambience_on'
    ENTRY_VIEW_EXIT = 'gui_lootbox_logistic_center_ambience_off'
    BENGAL_FIRE_OFF = 'gui_lootbox_logistic_center_bengal_fire_off'


class SeniorityInfoViewEvents(CONST_CONTAINER):
    ENTRY_VIEW_ENTER = 'gui_hangar_award_info_page_enter'
    ENTRY_VIEW_EXIT = 'gui_hangar_award_info_page_exit'


def playSound(eventName):
    if eventName:
        WWISE.WW_eventGlobal(eventName)