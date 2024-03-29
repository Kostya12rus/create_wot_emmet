# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/components/comp7.py
from comp7_ranks_common import MAIN_RANK_NAME, EXTRA_RANK_NAME
from constants import EntityCaptured
from gui.Scaleform.genConsts.COMP7_CONSTS import COMP7_CONSTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.battle_results.components import base, style
from gui.battle_results.components.vehicles import RegularVehicleStatValuesBlock, RegularVehicleStatsBlock, TeamStatsBlock, _getStunFilter
from constants import FAIRPLAY_VIOLATIONS
from gui.impl import backport
from gui.impl.gen.resources import R
from gui.impl.lobby.comp7 import comp7_shared, comp7_i18n_helpers
from gui.shared.formatters import text_styles
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

def getFormattedRating(rating):
    return ('{:+}').format(rating)


class PrestigePointsBlock(base.StatsBlock):
    __slots__ = ('isVisible', 'value', 'label', 'tooltip')

    def __init__(self, meta=None, field='', *path):
        super(PrestigePointsBlock, self).__init__(meta, field, *path)
        self.isVisible = False
        self.value = ''
        self.label = ''
        self.tooltip = ''

    def setRecord(self, result, reusable):
        achievedComp7Rating = result.get('avatar', {}).get('comp7RatingDelta', 0)
        if achievedComp7Rating is not None:
            self.isVisible = True
            self.value = text_styles.grandTitle(getFormattedRating(achievedComp7Rating))
            self.label = text_styles.creditsSmall(backport.text(R.strings.comp7.battleResult.personal.label()))
            self.tooltip = TOOLTIPS_CONSTANTS.COMP7_BATTLE_RESULTS_PRESTIGE_POINTS
        return


class EfficiencyTitleWithSkills(base.StatsItem):

    def _convert(self, value, reusable):
        return backport.text(R.strings.battle_results.common.battleEfficiencyWithSkills.title())


class IsDeserterFlag(base.StatsItem):

    def _convert(self, value, reusable):
        if reusable.personal.avatar.hasPenalties():
            penaltyName, _ = reusable.personal.avatar.getPenaltyDetails()
            if penaltyName == FAIRPLAY_VIOLATIONS.COMP7_DESERTER:
                return backport.text(R.strings.comp7.battleResult.header.deserter())


class Comp7RankBlock(base.StatsBlock):
    __slots__ = ('linkage', 'title', 'descr', 'icon', 'ratingDiff', 'hasProgressBar',
                 'progressBegin', 'progressCurrent', 'progressTotal', 'ratingTotal')
    __lobbyCtx = dependency.descriptor(ILobbyContext)

    def __init__(self, meta=None, field='', *path):
        super(Comp7RankBlock, self).__init__(meta, field, *path)
        self.linkage = None
        self.title = ''
        self.descr = ''
        self.icon = ''
        self.ratingDiff = ''
        self.hasProgressBar = False
        self.progressBegin = 0
        self.progressCurrent = 0
        self.progressTotal = 0
        self.ratingTotal = ''
        return

    def setRecord(self, result, reusable):
        avatarResults = result.get('avatar', {})
        achievedRating = avatarResults.get('comp7RatingDelta', 0)
        prevRating = avatarResults.get('comp7Rating', 0)
        prevRank, prevDivisionIdx = avatarResults.get('comp7Rank', (0, 0))
        prevDivision = comp7_shared.getPlayerDivisionByRankAndIndex(prevRank, prevDivisionIdx)
        currentRating = max(prevRating + achievedRating, 0)
        currentDivision = comp7_shared.getPlayerDivisionByRating(currentRating)
        currentRankValue = comp7_shared.getRankEnumValue(currentDivision)
        self.linkage = COMP7_CONSTS.COMP7_SUB_TASK_UI
        self.icon = backport.image(R.images.gui.maps.icons.comp7.ranks.c_64.num(currentRankValue)())
        self.title = self.__getTitle(currentDivision, prevDivision)
        self.descr = self.__getDescription(achievedRating, currentDivision)
        self.ratingDiff = self.__getRatingDiff(achievedRating)
        self.hasProgressBar = MAIN_RANK_NAME in currentDivision.tags
        self.progressBegin = currentDivision.range.begin
        self.progressCurrent = currentRating
        self.progressTotal = currentDivision.range.end + 1
        self.ratingTotal = text_styles.counter(backport.text(R.strings.comp7.battleResult.subTask.rating(), rating=currentRating))

    @classmethod
    def __getDescription(cls, achievedRating, division):
        isExtraRank = EXTRA_RANK_NAME in division.tags
        isElite = comp7_shared.isElite()
        extraPropertyName = ''
        if isExtraRank:
            extraPropertyName = 'Elite' if isElite else 'Master'
        propertyName = ('{}{}Rating').format('get' if achievedRating >= 0 else 'lose', extraPropertyName if extraPropertyName else '')
        ranksConfig = cls.__lobbyCtx.getServerSettings().comp7PrestigeRanksConfig
        ratingText = R.strings.comp7.battleResult.subTask.descr.dyn(propertyName)()
        return text_styles.main(backport.text(ratingText, topPercentage=ranksConfig.eliteRankPercent))

    @staticmethod
    def __getTitle(division, prevDivision):
        currentRankValue = comp7_shared.getRankEnumValue(division)
        currentDivisionValue = comp7_shared.getDivisionEnumValue(division)
        if EXTRA_RANK_NAME in division.tags:
            return text_styles.middleTitle(comp7_i18n_helpers.getRankLocale(currentRankValue))
        if division.dvsnID < prevDivision.dvsnID:
            title = R.strings.comp7.battleResult.subTask.title.c_raise()
        elif division.dvsnID > prevDivision.dvsnID:
            title = R.strings.comp7.battleResult.subTask.title.decrease()
        else:
            title = R.strings.comp7.battleResult.subTask.title.noRaise()
        return text_styles.middleTitle(backport.text(title, division=backport.text(R.strings.comp7.division.text(), division=comp7_i18n_helpers.getDivisionLocale(currentDivisionValue)), rank=comp7_i18n_helpers.getRankLocale(currentRankValue)))

    @staticmethod
    def __getRatingDiff(achievedRating):
        formattedRating = getFormattedRating(achievedRating)
        if achievedRating < 0:
            return text_styles.error(formattedRating)
        if achievedRating == 0:
            return text_styles.tutorial(formattedRating)
        return text_styles.bonusAppliedText(formattedRating)


class Comp7VehicleStatsBlock(RegularVehicleStatsBlock):
    __slots__ = ('prestigePoints', )

    def __init__(self, meta=None, field='', *path):
        super(Comp7VehicleStatsBlock, self).__init__(meta, field, *path)
        self.prestigePoints = 0

    def setRecord(self, result, reusable):
        super(Comp7VehicleStatsBlock, self).setRecord(result, reusable)
        self.prestigePoints = result.prestigePoints


class Comp7TeamStatsBlock(TeamStatsBlock):
    __slots__ = ()

    def __init__(self, meta=None, field='', *path):
        super(Comp7TeamStatsBlock, self).__init__(Comp7VehicleStatsBlock, meta, field, *path)


class Comp7VehicleStatValuesBlock(RegularVehicleStatValuesBlock):
    __slots__ = ('damageDealtBySkills', 'healed', 'capturedPointsOfInterest', 'roleSkillUsed')

    def setRecord(self, result, reusable):
        super(Comp7VehicleStatValuesBlock, self).setRecord(result, reusable)
        poiCaptured = result.entityCaptured
        self.damageDealtBySkills = style.getIntegralFormatIfNoEmpty(result.equipmentDamageDealt)
        self.healed = (result.healthRepair, result.alliedHealthRepair)
        self.capturedPointsOfInterest = style.getIntegralFormatIfNoEmpty(poiCaptured.get(EntityCaptured.POI_CAPTURABLE, 0))
        self.roleSkillUsed = style.getIntegralFormatIfNoEmpty(result.roleSkillUsed)


class AllComp7VehicleStatValuesBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        isPersonal, iterator = result
        add = self.addNextComponent
        stunFilter = _getStunFilter()
        for vehicle in iterator:
            block = Comp7VehicleStatValuesBlock()
            block.setPersonal(isPersonal)
            block.addFilters(stunFilter)
            block.setRecord(vehicle, reusable)
            add(block)


class PersonalVehiclesComp7StatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        info = reusable.getPersonalVehiclesInfo(result)
        add = self.addNextComponent
        stunFilter = _getStunFilter()
        for data in info.getVehiclesIterator():
            block = Comp7VehicleStatValuesBlock()
            block.setPersonal(True)
            block.addFilters(stunFilter)
            block.setRecord(data, reusable)
            add(block)