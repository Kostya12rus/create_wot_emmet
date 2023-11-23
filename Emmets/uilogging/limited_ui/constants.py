# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/limited_ui/constants.py
from enum import Enum
FEATURE = 'limited_ui'

class LimitedUILogItem(Enum):
    DISABLE_LIMITED_UI_BUTTON = 'disable_limited_ui_button'


class LimitedUILogScreenParent(Enum):
    SETTINGS_WINDOW = 'settings_window'


class LimitedUILogActions(Enum):
    CLICK = 'click'