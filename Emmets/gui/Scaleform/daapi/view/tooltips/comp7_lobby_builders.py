# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/comp7_lobby_builders.py
from gui.Scaleform.daapi.view.lobby.comp7.tooltips.comp7_selector_tooltip import Comp7SelectorTooltip, Comp7SelectorUnavailableTooltip
from gui.Scaleform.daapi.view.lobby.comp7.tooltips.comp7_calendar_day_tooltip import Comp7CalendarDayTooltip
from gui.Scaleform.daapi.view.lobby.comp7.tooltips.comp7_calendar_day_extended_tooltip import Comp7CalendarDayExtendedTooltip
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder
from gui.shared.tooltips.comp7_tooltips import RoleSkillLobbyTooltipData, BattleResultsPrestigePointsTooltip, BattleResultsTournamentPrestigePointsTooltip
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.COMP7_SELECTOR_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, Comp7SelectorTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.COMP7_SELECTOR_UNAVAILABLE_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, Comp7SelectorUnavailableTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.COMP7_CALENDAR_DAY_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, Comp7CalendarDayTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.COMP7_CALENDAR_DAY_EXTENDED_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, Comp7CalendarDayExtendedTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.COMP7_ROLE_SKILL_LOBBY_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, RoleSkillLobbyTooltipData(contexts.Comp7RoleSkillLobbyContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.COMP7_BATTLE_RESULTS_PRESTIGE_POINTS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, BattleResultsPrestigePointsTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.TOURNAMENT_COMP7_BATTLE_RESULTS_PRESTIGE_POINTS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, BattleResultsTournamentPrestigePointsTooltip(contexts.ToolTipContext(None))))