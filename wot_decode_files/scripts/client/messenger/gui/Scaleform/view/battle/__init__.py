# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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