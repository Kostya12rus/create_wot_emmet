# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/BattleHintsComponent.py
from BigWorld import DynamicScriptComponent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class BattleHintsComponent(DynamicScriptComponent):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def showHint(self, hintName, hintParams):
        battleHints = self.sessionProvider.dynamic.battleHints
        if battleHints:
            battleHints.showHint(hintName, {('param{}').format(i): t for i, t in enumerate(hintParams, 1)})

    def hideHint(self, hintName):
        battleHints = self.sessionProvider.dynamic.battleHints
        if battleHints:
            battleHints.hideHint(hintName)