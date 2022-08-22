# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/epic_battle/constants.py
from enum import Enum
FEATURE = 'epic_battle'
METRICS = 'metrics'

class EpicBattleLogActions(Enum):
    OPEN = 'open'
    CLOSE = 'close'
    CLICK = 'click'
    TOOLTIP_WATCHED = 'tooltip_watched'


class EpicBattleLogKeys(Enum):
    ABILITIES_CONFIRM = 'abilities_confirm'
    SETUP_VIEW = 'setup_view'
    DROP_SKILL_DIALOG_CONFIRM = 'drop_skill_dialog_confirm'
    BUTTON = 'button'
    HANGAR = 'hangar'


class EpicBattleLogButtons(Enum):
    INSTALL = 'install'
    NOT_INSTALL = 'not_install'
    CLOSE = 'close'
    RESERVES = 'reserves'
    CHECKBOX = 'checkbox'
    CANCEL = 'cancel'
    CONFIRM = 'confirm'


class EpicBattleLogAdditionalInfo(Enum):
    APPLY_TO_VEHICLE = 'apply_to_vehicle'
    APPLY_TO_CLASS = 'apply_to_class'