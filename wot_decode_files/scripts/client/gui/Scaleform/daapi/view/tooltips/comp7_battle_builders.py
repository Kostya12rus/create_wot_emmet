# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/comp7_battle_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import vehicle_roles
from gui.shared.tooltips.builders import DataBuilder, TooltipWindowBuilder
from gui.shared.tooltips.comp7_tooltips import RoleSkillBattleTooltipData
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.COMP7_ROLE_SKILL_BATTLE_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, RoleSkillBattleTooltipData(contexts.Comp7RoleSkillBattleContext())),
     TooltipWindowBuilder(TOOLTIPS_CONSTANTS.VEHICLE_ROLES, None, vehicle_roles.VehicleRolesTooltipContentWindowData(contexts.ToolTipContext(None))))