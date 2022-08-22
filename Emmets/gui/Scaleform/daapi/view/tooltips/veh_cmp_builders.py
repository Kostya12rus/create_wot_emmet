# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/veh_cmp_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import veh_cmp
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.VEH_CMP_CUSTOMIZATION, TOOLTIPS_CONSTANTS.VEH_CMP_CUSTOMIZATION_UI, veh_cmp.VehCmpCustomizationTooltip(contexts.HangarParamContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.VEH_CMP_SKILLS, TOOLTIPS_CONSTANTS.VEH_CMP_SKILLS_UI, veh_cmp.VehCmpSkillsTooltip(contexts.HangarParamContext())))