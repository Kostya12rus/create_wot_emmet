# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic/full_stats.py
import BigWorld
from gui.Scaleform.daapi.view.meta.EpicFullStatsMeta import EpicFullStatsMeta
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from helpers import i18n

class EpicFullStatsComponent(EpicFullStatsMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _populate(self):
        super(EpicFullStatsComponent, self)._populate()
        self.as_initializeTextS(i18n.makeString(EPIC_BATTLE.TAB_SCREEN_SHOW_MY_LANE).upper(), i18n.makeString(EPIC_BATTLE.TAB_SCREEN_SHOW_ALL_LANES).upper())
        BigWorld.player().arena.componentSystem.playerDataComponent.onCrewRolesFactorUpdated += self.__setGeneralBonus

    def _dispose(self):
        super(EpicFullStatsComponent, self)._dispose()
        arena = BigWorld.player().arena if hasattr(BigWorld.player(), 'arena') else None
        if arena and hasattr(arena, 'componentSystem'):
            componentSystem = BigWorld.player().arena.componentSystem
            if componentSystem:
                componentSystem.playerDataComponent.onCrewRolesFactorUpdated -= self.__setGeneralBonus
        return

    def __setGeneralBonus(self, newFactor, allyVehID=None, allyNewRank=None):
        self.as_setGeneralBonusS(newFactor)