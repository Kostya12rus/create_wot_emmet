# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/common/personal_reserves/personal_reserves_shared_constants.py
import typing
from backports.functools_lru_cache import lru_cache
from constants import FORT_ORDER_TYPE
from goodies.goodie_constants import PR2BoosterIDs, GOODIE_RESOURCE_TYPE, MAX_ACTIVE_PERSONAL_BOOSTERS, MAX_ACTIVE_EVENT_BOOSTERS, GOODIE_STATE, BoosterCategory
from gui.impl.gen.view_models.common.personal_reserves.booster_model import ReserveType, ReserveState
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.goodies import IGoodiesCache
if typing.TYPE_CHECKING:
    from gui.goodies import GoodiesCache
    from gui.goodies.goodie_items import Booster
    from typing import Set
PERSONAL_RESOURCE_ORDER = [GOODIE_RESOURCE_TYPE.XP, GOODIE_RESOURCE_TYPE.CREDITS, GOODIE_RESOURCE_TYPE.FREE_XP_CREW_XP]
EVENT_RESOURCE_ORDER = [
 GOODIE_RESOURCE_TYPE.FL_XP]
CLAN_RESOURCE_ORDER_BY_GROUP = [
 (
  GOODIE_RESOURCE_TYPE.FREE_XP,
  GOODIE_RESOURCE_TYPE.CREW_XP),
 (
  GOODIE_RESOURCE_TYPE.CREDITS,
  GOODIE_RESOURCE_TYPE.XP)]
FRONT_LINE_BOOSTER_ID = 111001
BATTLE_XP_PREMIUM_BOOSTER_ID = PR2BoosterIDs.XP
CREDITS_PREMIUM_BOOSTER_ID = PR2BoosterIDs.CRED
COMBINED_XP_BOOSTER_ID = PR2BoosterIDs.XP_CREW_FREE
PREMIUM_BOOSTER_IDS = [
 BATTLE_XP_PREMIUM_BOOSTER_ID, CREDITS_PREMIUM_BOOSTER_ID, COMBINED_XP_BOOSTER_ID]
UNATTAINABLE_BOOSTER_IDS = [
 CREDITS_PREMIUM_BOOSTER_ID]
EVENT_BOOSTER_IDS = [
 FRONT_LINE_BOOSTER_ID]
BOOST_CATEGORY_TO_RESERVE_TYPE_LOOKUP = {BoosterCategory.PERSONAL: ReserveType.PERSONAL, 
   BoosterCategory.EVENT: ReserveType.EVENT, 
   BoosterCategory.CLAN: ReserveType.CLAN}
BOOSTER_STATE_TO_BOOSTER_MODEL_STATE = {GOODIE_STATE.INACTIVE: ReserveState.INACTIVE, 
   GOODIE_STATE.ACTIVE: ReserveState.ACTIVE, 
   GOODIE_STATE.USED: ReserveState.USED}
BUY_AND_ACTIVATE_TIMEOUT = 30.0
GOODIES_TYPE_TO_CLAN_BOOSTERS = {GOODIE_RESOURCE_TYPE.CREDITS: [
                                FORT_ORDER_TYPE.COMBAT_PAYMENTS, FORT_ORDER_TYPE.COMBAT_PAYMENTS_2_0], 
   GOODIE_RESOURCE_TYPE.XP: [
                           FORT_ORDER_TYPE.TACTICAL_TRAINING, FORT_ORDER_TYPE.TACTICAL_TRAINING_2_0], 
   GOODIE_RESOURCE_TYPE.FREE_XP: [
                                FORT_ORDER_TYPE.MILITARY_EXERCISES, FORT_ORDER_TYPE.MILITARY_EXERCISES_2_0], 
   GOODIE_RESOURCE_TYPE.CREW_XP: [
                                FORT_ORDER_TYPE.ADDITIONAL_BRIEFING, FORT_ORDER_TYPE.ADDITIONAL_BRIEFING_2_0]}
MAX_ACTIVATED_BY_CATEGORY = {BoosterCategory.PERSONAL: MAX_ACTIVE_PERSONAL_BOOSTERS, 
   BoosterCategory.EVENT: MAX_ACTIVE_EVENT_BOOSTERS, 
   BoosterCategory.CLAN: 2}
BOOSTERS_CATEGORY_VIEW_ORDER = (
 BoosterCategory.PERSONAL, BoosterCategory.EVENT, BoosterCategory.CLAN)

@lru_cache()
@dependency.replace_none_kwargs(goodiesCache=IGoodiesCache)
def getAllBoosterIds(goodiesCache=None):
    enabledBoosters = goodiesCache.getBoosters(criteria=REQ_CRITERIA.BOOSTER.ENABLED)
    return set(enabledBoosters.keys())