# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/customization/constants.py


class CustomizationModes(object):
    NONE = -1
    CUSTOM = 1
    STYLED = 2
    EDITABLE_STYLE = 3
    ALL = (
     CUSTOM, STYLED, EDITABLE_STYLE)


class CustomizationModeSource(object):
    UNDEFINED = -1
    BOTTOM_PANEL = 1
    CAROUSEL = 2
    CONTEXT_MENU = 3
    PROPERTIES_SHEET = 4
    NOTIFICATION = 5
    REWARD_WINDOW = 6