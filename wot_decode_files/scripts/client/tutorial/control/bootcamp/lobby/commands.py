# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/bootcamp/lobby/commands.py
from helpers import dependency
from skeletons.tutorial import ITutorialLoader
from tutorial.logger import LOG_ERROR

@dependency.replace_none_kwargs(tutorialLoader=ITutorialLoader)
def overrideHangarMenuButtons(buttonsListVarID=None, tutorialLoader=None):
    tutorialLoader.gui.overrideHangarMenuButtons(_getListByVarID(buttonsListVarID, tutorialLoader))


@dependency.replace_none_kwargs(tutorialLoader=ITutorialLoader)
def overrideHeaderMenuButtons(buttonsListVarID=None, tutorialLoader=None):
    tutorialLoader.gui.overrideHeaderMenuButtons(_getListByVarID(buttonsListVarID, tutorialLoader))


@dependency.replace_none_kwargs(tutorialLoader=ITutorialLoader)
def setHangarHeaderEnabled(enabled, tutorialLoader=None):
    tutorialLoader.gui.setHangarHeaderEnabled(enabled)


@dependency.replace_none_kwargs(tutorialLoader=ITutorialLoader)
def overrideBattleSelectorHint(overrideType=None, tutorialLoader=None):
    tutorialLoader.gui.overrideBattleSelectorHint(overrideType)


def _getListByVarID(varID, tutorialLoader):
    if varID is not None:
        tutorial = tutorialLoader.tutorial
        varVal = tutorial.getVars().get(varID)
        if varVal is None:
            LOG_ERROR('variable not found', varID)
            return
        if isinstance(varVal, list):
            return varVal
        LOG_ERROR('variable value is not a list', varID, varVal)
    return