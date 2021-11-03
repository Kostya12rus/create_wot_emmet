# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/go_back_helper.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl import backport
from gui.impl.gen import R
from shared_utils import CONST_CONTAINER
VEHICLE_PREVIEW_ALIASES = (
 VIEW_ALIAS.VEHICLE_PREVIEW, VIEW_ALIAS.HERO_VEHICLE_PREVIEW, VIEW_ALIAS.OFFER_GIFT_VEHICLE_PREVIEW,
 VIEW_ALIAS.TRADE_IN_VEHICLE_PREVIEW, VIEW_ALIAS.PERSONAL_TRADE_IN_VEHICLE_PREVIEW,
 VIEW_ALIAS.MARATHON_VEHICLE_PREVIEW, VIEW_ALIAS.CONFIGURABLE_VEHICLE_PREVIEW,
 VIEW_ALIAS.EVENT_KING_REWARD_PREVIEW)

class BackButtonContextKeys(CONST_CONTAINER):
    BLUEPRINT_MODE = 'blueprintMode'
    NATION = 'nation'
    EXIT = 'exit'
    ROOT_CD = 'rootCD'


def getBackBtnDescription(exitEvent, previewView, vehicleName=''):
    descriptionLabels = R.strings.menu.viewHeader.backBtn.descrLabel
    alias = descriptionLabels.hangar
    if previewView == VIEW_ALIAS.LOBBY_RESEARCH:
        alias = descriptionLabels.research
    elif previewView == VIEW_ALIAS.LOBBY_TECHTREE:
        nation = exitEvent.ctx[BackButtonContextKeys.NATION]
        blueprintMode = exitEvent.ctx.get(BackButtonContextKeys.BLUEPRINT_MODE, False)
        if blueprintMode:
            alias = descriptionLabels.techtree.dyn(nation).blueprints
        else:
            alias = descriptionLabels.techtree.dyn(nation)
    elif previewView in VEHICLE_PREVIEW_ALIASES:
        alias = descriptionLabels.preview
    ctx = {'tankName': vehicleName}
    return backport.text(alias(), **ctx)