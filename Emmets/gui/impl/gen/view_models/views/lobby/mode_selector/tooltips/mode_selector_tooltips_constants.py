# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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
    EPIC_BATTLE_WIDGET_INFO = 'epicBattleWidgetInfo'
    FUN_RANDOM_CALENDAR_TOOLTIP = 'funRandomModeSelectorCalendarDay'
    FUN_RANDOM_REWARDS = 'funRandomRewards'
    NOT_SUITABLE_VEHICLES_TOOLTIP = 'notSuitableVehiclesTooltip'
    COMP7_CALENDAR_DAY_EXTENDED_INFO = 'comp7CalendarDayExtendedInfo'

    def __init__(self, properties=0, commands=0):
        super(ModeSelectorTooltipsConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ModeSelectorTooltipsConstants, self)._initialize()