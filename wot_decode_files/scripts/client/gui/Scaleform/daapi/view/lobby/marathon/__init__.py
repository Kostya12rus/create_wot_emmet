# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/marathon/__init__.py
from gui.Scaleform.framework import ScopeTemplates, ComponentSettings
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.marathon.marathon_entry_point import MarathonEntryPointWrapper
    return (
     ComponentSettings(HANGAR_ALIASES.MARATHON_ENTRY_POINT, MarathonEntryPointWrapper, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()