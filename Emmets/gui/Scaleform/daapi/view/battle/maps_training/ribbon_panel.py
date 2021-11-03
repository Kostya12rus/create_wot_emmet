# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/maps_training/ribbon_panel.py
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES as _BET
_PROHIB_BATTLE_EFFICIENCY_TYPES = (_BET.CAPTURE, _BET.DEFENCE, _BET.BASE_CAPTURE_BLOCKED)

class MapsTrainingRibbonPanel(BattleRibbonsPanel):

    def _shouldShowRibbon(self, ribbon):
        if ribbon.getType() in _PROHIB_BATTLE_EFFICIENCY_TYPES:
            return False
        return super(MapsTrainingRibbonPanel, self)._shouldShowRibbon(ribbon)