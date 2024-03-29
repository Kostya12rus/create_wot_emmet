# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic/full_stats.py
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