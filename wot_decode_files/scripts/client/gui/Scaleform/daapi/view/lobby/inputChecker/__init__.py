# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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