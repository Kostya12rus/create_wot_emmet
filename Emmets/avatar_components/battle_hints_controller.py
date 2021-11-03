# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/battle_hints_controller.py
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class BattleHintsController(object):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def handleKey(self, isDown, key, mods):
        pass

    def showHint(self, hintName, hintParams):
        battleHints = self.guiSessionProvider.dynamic.battleHints
        if battleHints:
            battleHints.showHint(hintName, hintParams)

    def hideHint(self, hintName):
        battleHints = self.guiSessionProvider.dynamic.battleHints
        if battleHints:
            battleHints.hideHint(hintName)