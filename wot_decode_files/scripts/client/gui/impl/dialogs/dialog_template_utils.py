# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/dialogs/dialog_template_utils.py
import typing, constants
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.impl import backport
from gui.impl.gen_utils import DynAccessor
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from gui.impl.pub import ViewImpl

def toString(value):
    if isinstance(value, DynAccessor):
        return backport.text(value())
    if isinstance(value, (long, int)):
        return backport.text(value)
    return value


def findDialogTemplatesByUniqueID(uniqueID):
    from gui.impl.dialogs.dialog_template import DialogTemplateView
    guiLoader = dependency.instance(IGuiLoader)

    def predicate(view):
        return isinstance(view, DialogTemplateView) and view.dialogUniqueID == uniqueID

    return guiLoader.windowsManager.findViews(predicate)


def checkDialogTemplateIsOpened(uniqueID):
    return len(findDialogTemplatesByUniqueID(uniqueID)) != 0


def closeDialogTemplate(uniqueID):
    for dlg in findDialogTemplatesByUniqueID(uniqueID):
        dlg.destroyWindow()


def getCurrencyTooltipAlias(currency):
    if constants.IS_SINGAPORE and currency in CURRENCIES_CONSTANTS.SINGAPORE_ALTERNATIVE_CURRENCIES_SET:
        return currency + 'StatsFullScreen'
    return currency + 'InfoFullScreen'