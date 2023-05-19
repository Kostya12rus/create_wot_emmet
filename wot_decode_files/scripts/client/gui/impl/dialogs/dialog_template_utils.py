# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/dialogs/dialog_template_utils.py
import typing, constants
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.impl import backport
from gui.impl.gen_utils import DynAccessor
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from typing import Union

def toString(value):
    if isinstance(value, DynAccessor):
        return backport.text(value())
    if isinstance(value, (long, int)):
        return backport.text(value)
    return value


def checkDialogTemplateIsOpened(uniqueID):
    from gui.impl.dialogs.dialog_template import DialogTemplateView
    guiLoader = dependency.instance(IGuiLoader)

    def predicate(view):
        return isinstance(view, DialogTemplateView) and view.uniqueID == uniqueID

    return len(guiLoader.windowsManager.findViews(predicate)) != 0


def getCurrencyTooltipAlias(currency):
    if constants.IS_SINGAPORE and currency in CURRENCIES_CONSTANTS.SINGAPORE_ALTERNATIVE_CURRENCIES_SET:
        return currency + 'StatsFullScreen'
    return currency + 'InfoFullScreen'