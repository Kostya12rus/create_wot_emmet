# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/personal_missions_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import personal_missions
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.PERSONAL_QUESTS_PREVIEW, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.PersonalMissionPreviewTooltipData(contexts.PersonalMissionContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.PERSONAL_MISSIONS_TANKWOMAN, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.TankwomanTooltipData(contexts.PersonalMissionContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.PERSONAL_MISSIONS_TANKMODULE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.TankModuleTooltipData(contexts.PersonalMissionContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.FREE_SHEET, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.FreeSheetTooltip(contexts.PersonalMissionCampaignContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.FREE_SHEET_RETURN, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.FreeSheetReturnTooltip(contexts.PersonalMissionCampaignContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.FREE_SHEET_NOT_ENOUGH, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.FreeSheetNotEnoughTooltip(contexts.PersonalMissionCampaignContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.FREE_SHEET_USED, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.FreeSheetUsedTooltip(contexts.PersonalMissionCampaignContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BADGE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.BadgeTooltipData(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.BADGE_LOYAL_SERVICE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.LoyalServiceTooltipData(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.OPERATION, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.OperationTooltipData(contexts.PersonalMissionOperationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.PERSONAL_MISSION_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.PersonalMissionInfoTooltipData(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.PERSONAL_MISSIONS_MAP_REGION, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.PersonalMissionsMapRegionTooltipData(contexts.PersonalMissionContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.OPERATIONS_CHAIN_DETAILS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.OperationsChainDetailsTooltipData(contexts.PersonalMissionContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.OPERATION_POSTPONED, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, personal_missions.OperationPostponedTooltipData(contexts.PersonalMissionOperationContext())))