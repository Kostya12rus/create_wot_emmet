# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/genConsts/TUTORIAL_TRIGGER_TYPES.py


class TUTORIAL_TRIGGER_TYPES(object):
    CLICK_TYPE = 'click'
    CLICK_OUTSIDE_TYPE = 'clickOutside'
    ESCAPE = 'escape'
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    ENABLED_CHANGE = 'enabled_change'
    VISIBLE_CHANGE = 'visible_change'
    ALL = [CLICK_TYPE, CLICK_OUTSIDE_TYPE, ESCAPE, ENABLED, DISABLED, ENABLED_CHANGE, 
     VISIBLE_CHANGE]