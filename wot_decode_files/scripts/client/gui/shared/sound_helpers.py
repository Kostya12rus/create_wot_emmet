# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/sound_helpers.py
import SoundGroups, WWISE
from shared_utils import CONST_CONTAINER

class SliderSoundEvents(CONST_CONTAINER):
    RTPC_PROGRESS_BAR = 'RTPC_ext_ammo_progress_bar'
    SLIDER_SINGLE_PLUS = 'cons_ammo_single_plus'
    SLIDER_SINGLE_MINUS = 'cons_ammo_single_minus'


def playSliderUpdateSound(oldCount, newCount, totalCount):
    WWISE.WW_setRTPCBus(SliderSoundEvents.RTPC_PROGRESS_BAR, newCount * 100.0 / totalCount)
    if newCount > oldCount:
        SoundGroups.g_instance.playSound2D(SliderSoundEvents.SLIDER_SINGLE_PLUS)
    elif newCount < oldCount:
        SoundGroups.g_instance.playSound2D(SliderSoundEvents.SLIDER_SINGLE_MINUS)