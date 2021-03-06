# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/account_completion/constants.py
from enum import Enum

class LogGroup(str, Enum):
    NICKNAME = 'nickname'
    CREDENTIALS = 'credentials'
    COMPLETE = 'complete'
    CONFIRM = 'confirm'
    MENU = 'menu'
    SKIP_NICKNAME_DIALOG = 'skip_nickname_dialog'
    ACCOUNT_DASHBOARD = 'account_dashboard'
    PLAYER_NAME = 'player_name'


class LogActions(Enum):
    CLOSE_CLICKED = 'close_clicked'
    CONFIRM_CLICKED = 'confirm_clicked'
    CLOSED = 'closed'
    CANCEL_CLICKED = 'cancel_clicked'
    RENAME_CLICKED = 'rename_clicked'
    ESCAPE_PRESSED = 'escape_pressed'
    CONTINUE_CLICKED = 'continue_clicked'
    SETTINGS_CLICKED = 'settings_clicked'
    QUIT_CLICKED = 'quit_clicked'
    RETURN_CLICKED = 'return_clicked'
    CLICKED = 'clicked'


class ViewClosingResult(str, Enum):
    CLOSED = 'closed'
    SUCCESS = 'success'
    BACK_TO_CREDENTIALS = 'back_to_credentials'


FEATURE = 'in_game_registration'