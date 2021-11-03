# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/tooltips/mode_selector_tooltips_constants.py
from frameworks.wulf import ViewModel

class ModeSelectorTooltipsConstants(ViewModel):
    __slots__ = ()
    DISABLED_TOOLTIP = 'disabledTooltip'
    RANDOM_BP_PAUSED_TOOLTIP = 'randomBPPausedTooltip'
    RANKED_CALENDAR_DAY_INFO_TOOLTIP = 'rankedCalendarDayInfoExtended'
    RANKED_STEP_TOOLTIP = 'rankedStep'
    RANKED_BATTLES_RANK_TOOLTIP = 'rankedBattlesRank'
    RANKED_BATTLES_BONUS_TOOLTIP = 'rankedBattlesBonus'
    RANKED_BATTLES_LEAGUE_TOOLTIP = 'rankedBattlesLeague'
    RANKED_BATTLES_EFFICIENCY_TOOLTIP = 'rankedBattlesEfficiency'
    RANKED_BATTLES_POSITION_TOOLTIP = 'rankedBattlesPosition'
    CALENDAR_TOOLTIP = 'calendarTooltip'
    MAPBOX_CALENDAR_TOOLTIP = 'mapboxCalendar'
    EPIC_BATTLE_CALENDAR_TOOLTIP = 'epicBattleCalendarTooltip'

    def __init__(self, properties=0, commands=0):
        super(ModeSelectorTooltipsConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ModeSelectorTooltipsConstants, self)._initialize()