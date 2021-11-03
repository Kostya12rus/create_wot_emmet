# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/inputChecker/__init__.py
from gui.Scaleform.daapi.view.lobby.inputChecker.InputChecker import InputChecker
from gui.Scaleform.framework import ScopeTemplates, ComponentSettings

class INPUT_CHECKER_ALIASES(object):
    INPUT_CHECKER = 'inputCheckerComponent'


def getContextMenuHandlers():
    return ()


def getViewSettings():
    return (
     ComponentSettings(INPUT_CHECKER_ALIASES.INPUT_CHECKER, InputChecker, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()