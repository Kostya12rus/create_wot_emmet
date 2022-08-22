# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/mode_selector/constants.py


class LOG_KEYS(object):
    RANDOM_CARD_FILTER = 'random_card_filter'
    ENTRY_POINT = 'entry_point'
    MS_WINDOW = 'ms_window'


class LOG_ACTIONS(object):
    CHANGED = 'changed'
    CARD_CLICKED = 'card_clicked'
    INFO_PAGE_ICON_CLICKED = 'info_page_icon_clicked'
    CLOSED = 'closed'
    OPENED = 'opened'
    TOOLTIP_WATCHED = 'tooltip_watched'


class LOG_CLOSE_DETAILS(object):
    CARD_CLICKED = 'card_clicked'
    OTHER = 'other'
    SELECTOR = 'selector'


FEATURE = 'mode_selector_2'
SELECTOR_BUTTON_TOOLTIP_LOG_ID = 'modeSelectorBtn'