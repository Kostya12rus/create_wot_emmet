# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/personal_reserves/__init__.py
from gui.clans.clan_helpers import getStrongholdClanCardUrl
from helpers.dependency import replace_none_kwargs
from gui.goodies.goodie_items import _CLAN_RESERVE_TO_GUI_TYPE
from gui.shared.event_dispatcher import showStrongholds
from skeletons.gui.goodies import IGoodiesCache

@replace_none_kwargs(goodiesCache=IGoodiesCache)
def boosterActivationFlow(boosterId, goodiesCache=None):
    if boosterId in _CLAN_RESERVE_TO_GUI_TYPE:
        showStrongholds(getStrongholdClanCardUrl(), reloadView=True)
        return
    from gui.shared.gui_items.items_actions import factory
    booster = goodiesCache.getBooster(boosterId)
    if booster.isInAccount:
        actionId = factory.ACTIVATE_BOOSTER
    else:
        actionId = factory.BUY_AND_ACTIVATE_BOOSTER
    factory.doAction(actionId, booster)