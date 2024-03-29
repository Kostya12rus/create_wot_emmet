# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/achievement_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import achievement
from gui.shared.tooltips import builders
from gui.shared.tooltips import contexts
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     builders.DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_STATS_ACHIEVS, TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI, achievement.AchievementTooltipData(contexts.BattleResultContext())),
     builders.DataBuilder(TOOLTIPS_CONSTANTS.SHOP_ACHIEVEMENT, TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI, achievement.AchievementTooltipData(contexts.ShopAchievementContext())),
     builders.DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_STATS_MARKS_ON_GUN_ACHIEVEMENT, TOOLTIPS_CONSTANTS.MARKS_ON_GUN_UI, achievement.AchievementTooltipData(contexts.BattleResultMarksOnGunContext())),
     builders.DataBuilder(TOOLTIPS_CONSTANTS.ACHIEVEMENT, TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI, achievement.AchievementTooltipData(contexts.ProfileContext())),
     builders.DataBuilder(TOOLTIPS_CONSTANTS.MARKS_ON_GUN_ACHIEVEMENT, TOOLTIPS_CONSTANTS.MARKS_ON_GUN_UI, achievement.AchievementTooltipData(contexts.ProfileContext())),
     builders.DataBuilder(TOOLTIPS_CONSTANTS.GLOBAL_RATING, TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI, achievement.GlobalRatingTooltipData(contexts.ProfileContext())),
     builders.DataBuilder(TOOLTIPS_CONSTANTS.MARK_OF_MASTERY, TOOLTIPS_CONSTANTS.MARK_OF_MASTERY_UI, achievement.AchievementTooltipData(contexts.BattleResultMarkOfMasteryContext(fieldsToExclude=('showCondSeparator', )))),
     builders.DataBuilder(TOOLTIPS_CONSTANTS.SHOP_BADGE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, achievement.BadgeTooltipData(contexts.BadgeContext(None))),
     builders.DataBuilder(TOOLTIPS_CONSTANTS.REFERRAL_BADGE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, achievement.BadgeTooltipData(contexts.ReferralProgramBadgeContext(None))),
     builders.SimpleBuilder('achievementAttr', TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI))