# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/battle/__init__.py
from gui.Scaleform.framework import ScopeTemplates, ComponentSettings

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from messenger.gui.Scaleform.view.battle import messenger_view
    from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
    return (
     ComponentSettings(BATTLE_VIEW_ALIASES.BATTLE_MESSENGER, messenger_view.BattleMessengerView, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()