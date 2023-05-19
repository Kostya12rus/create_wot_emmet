# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/go_back_helper.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VEHICLE_PREVIEW_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from shared_utils import CONST_CONTAINER

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