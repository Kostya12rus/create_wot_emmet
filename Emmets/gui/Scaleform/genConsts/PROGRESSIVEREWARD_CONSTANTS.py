# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/genConsts/PROGRESSIVEREWARD_CONSTANTS.py


class PROGRESSIVEREWARD_CONSTANTS(object):
    STATE_NOT_RECEIVED = 'not_received'
    STATE_OPENED = 'opened'
    STATE_PROB_MIN = 'prob_min'
    STATE_PROB_MED = 'prob_med'
    STATE_PROB_MAX = 'prob_max'
    STATE_RECEIVED = 'received'
    STATES = [STATE_NOT_RECEIVED, STATE_OPENED, STATE_PROB_MIN, STATE_PROB_MED, STATE_PROB_MAX, STATE_RECEIVED]
    REWARD_TYPE_SMALL = 'small'
    REWARD_TYPE_BIG = 'big'
    REWARD_TYPE_SMALL_HIDDEN = 'small_hidden'
    REWARD_TYPE_BIG_HIDDEN = 'big_hidden'
    REWARD_TYPES = [REWARD_TYPE_SMALL, REWARD_TYPE_BIG]
    WIDGET_LAYOUT_H = 0
    WIDGET_LAYOUT_V = 1
    WIDGET_LAYOUT = [WIDGET_LAYOUT_H, WIDGET_LAYOUT_V]