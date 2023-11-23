# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/selectable_reward/constants.py
from enum import Enum
from battle_pass_common import BATTLE_PASS_OFFER_TOKEN_PREFIX
from gui.ranked_battles.constants import YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX
from epic_constants import EPIC_OFFER_TOKEN_PREFIX

class Features(Enum):
    UNDEFINED = 0
    BATTLE_PASS = 1
    RANKED = 2
    EPIC = 3


FEATURE_TO_PREFIX = {Features.BATTLE_PASS: BATTLE_PASS_OFFER_TOKEN_PREFIX, 
   Features.RANKED: YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX, 
   Features.EPIC: EPIC_OFFER_TOKEN_PREFIX}
SELECTABLE_BONUS_NAME = 'selectableBonus'