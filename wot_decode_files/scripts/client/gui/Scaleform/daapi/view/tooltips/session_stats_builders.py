# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/session_stats_builders.py
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_tooltips import SessionStatsTankInfo, SessionStatsEfficiencyParam
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.SESSION_STATS_TANK_INFO, TOOLTIPS_CONSTANTS.SESSION_STATS_TANK_INFO_UI, SessionStatsTankInfo(contexts.SessionStatsContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.SESSION_STATS_EFFICIENCY_PARAM, TOOLTIPS_CONSTANTS.SESSION_STATS_EFFICIENCY_PARAM_UI, SessionStatsEfficiencyParam(contexts.SessionStatsContext())))