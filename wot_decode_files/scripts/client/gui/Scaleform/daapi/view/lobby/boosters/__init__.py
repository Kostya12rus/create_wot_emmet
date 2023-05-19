# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/boosters/__init__.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates, ComponentSettings

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.boosters.BoostersPanelComponent import BoostersPanelComponent
    return (
     ComponentSettings(VIEW_ALIAS.BOOSTERS_PANEL, BoostersPanelComponent, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()