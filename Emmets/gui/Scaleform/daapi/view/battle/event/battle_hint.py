# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/battle_hint.py
from gui.Scaleform.daapi.view.meta.BattleHintMeta import BattleHintMeta
from gui.battle_control.controllers.battle_hints_ctrl import BattleHintComponent

class BattleHint(BattleHintComponent, BattleHintMeta):

    def _showHint(self, data):
        self.as_showHintS(data)

    def _hideHint(self):
        if self.currentHint:
            self.as_hideHintS()