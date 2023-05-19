# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/page.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage, COMMON_CLASSIC_CONFIG, EXTENDED_CLASSIC_CONFIG
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
_EPIC_RANDOM_CLASSICS_COMPONENTS = COMMON_CLASSIC_CONFIG
_EPIC_RANDOM_EXTENDED_COMPONENTS = EXTENDED_CLASSIC_CONFIG

class EpicRandomPage(ClassicPage):

    def __init__(self, components=None, external=None, fullStatsAlias=BATTLE_VIEW_ALIASES.FULL_STATS):
        if components is None:
            components = _EPIC_RANDOM_CLASSICS_COMPONENTS if self.sessionProvider.isReplayPlaying else _EPIC_RANDOM_EXTENDED_COMPONENTS
        super(EpicRandomPage, self).__init__(components=components, external=external, fullStatsAlias=fullStatsAlias)
        return

    def _onBattleLoadingStart(self):
        super(EpicRandomPage, self)._onBattleLoadingStart()
        if not self.sessionProvider.isReplayPlaying:
            self.app.enterGuiControlMode(BATTLE_VIEW_ALIASES.BATTLE_LOADING)

    def _onBattleLoadingFinish(self):
        super(EpicRandomPage, self)._onBattleLoadingFinish()
        if not self.sessionProvider.isReplayPlaying:
            self.app.leaveGuiControlMode(BATTLE_VIEW_ALIASES.BATTLE_LOADING)