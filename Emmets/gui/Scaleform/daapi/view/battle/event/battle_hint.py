# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/battle_hint.py
from gui.battle_control.controllers.battle_hints_ctrl import BattleHintComponent
from gui.Scaleform.daapi.view.meta.BattleHintMeta import BattleHintMeta

class BattleHint(BattleHintComponent, BattleHintMeta):

    def _showHint(self, hint, voData):
        hintName = hint.name
        self.as_showHintS(hintName, voData)

    def _hideHint(self):
        self.as_hideHintS()

    def _finishHint(self):
        self.as_closeHintS()