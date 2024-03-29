# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/ranked_battles/ranked_builders/divisions_vos.py
import typing
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.ranked_battles import ranked_formatters
from gui.ranked_battles.ranked_builders import shared_vos
from gui.shared.formatters import text_styles
if typing.TYPE_CHECKING:
    from gui.ranked_battles.ranked_models import Division, Rank

def getDivisionVO(division):
    alias = _getAlias(division)
    divisionVO = shared_vos.getDivisionVO(division)
    divisionVO.update({'name': text_styles.middleTitle(divisionVO['name']), 
       'linkage': alias, 
       'viewId': alias})
    return divisionVO


def getDivisionStatsVO(divisionEfficiencyPercent, seasonEfficiencyPercent):
    return {'divisionEfficiency': shared_vos.getStatVO(ranked_formatters.getFloatPercentStrStat(divisionEfficiencyPercent), 'divisionEfficiency', 'divisionEfficiency', 'divisionEfficiency'), 
       'seasonEfficiency': shared_vos.getStatVO(ranked_formatters.getFloatPercentStrStat(seasonEfficiencyPercent), 'seasonEfficiency', 'efficiency', 'seasonEfficiency')}


def getRankVO(rank):
    steps = []
    achivedStepsCount = rank.getAchievedStepsCount()
    for idx in range(1, rank.getStepsCountToAchieve() + 1):
        if idx <= achivedStepsCount:
            steps.append(RANKEDBATTLES_ALIASES.STEP_RECEIVED_STATE)
        else:
            steps.append(RANKEDBATTLES_ALIASES.STEP_NOT_RECEIVED_STATE)

    shieldVO = None
    shieldStatus = rank.getShieldStatus()
    if shieldStatus is not None and shieldStatus.hp > 0:
        shortcut = R.images.gui.maps.icons.rankedBattles.ranks.shields
        hpShortcut = R.images.gui.maps.icons.rankedBattles.ranks.shields.plate
        shieldKey = ('c_{}').format(shieldStatus.hp)
        shieldVO = {'smallImageSrc': backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_SMALL)()), 
           'bigImageSrc': backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_BIG)()), 
           'hugeImageSrc': backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_HUGE)()), 
           'smallPlateSrc': backport.image(hpShortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_SMALL).dyn(shieldKey)()), 
           'mediumPlateSrc': backport.image(hpShortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_MEDIUM).dyn(shieldKey)()), 
           'bigPlateSrc': backport.image(hpShortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_BIG).dyn(shieldKey)()), 
           'hugePlateSrc': backport.image(hpShortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_HUGE).dyn(shieldKey)())}
    elif rank.isVisualUnburnable():
        shortcut = R.images.gui.maps.icons.rankedBattles.ranks.unburnable
        shieldVO = {'smallImageSrc': backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_SMALL)()), 
           'bigImageSrc': backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_BIG)()), 
           'hugeImageSrc': backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_HUGE)())}
    return {'stepsData': {'steps': steps, 
                     'infoText': ''}, 
       'rankLabel': backport.text(R.strings.ranked_battles.rankedBattleMainView.divisions.currentRank()) if rank.isCurrent() else '', 
       'smallImageSrc': rank.getIcon(RANKEDBATTLES_ALIASES.WIDGET_SMALL), 
       'bigImageSrc': rank.getIcon(RANKEDBATTLES_ALIASES.WIDGET_BIG), 
       'hugeImageSrc': rank.getIcon(RANKEDBATTLES_ALIASES.WIDGET_HUGE), 
       'isAcquired': rank.isAcquired(), 
       'rankID': str(rank.getID()), 
       'hasTooltip': True, 
       'shield': shieldVO}


def _getAlias(division):
    if division.isQualification():
        return RANKEDBATTLES_ALIASES.RANKED_BATTLES_DIVISIONS_QUALIFICATION_UI
    return RANKEDBATTLES_ALIASES.RANKED_BATTLES_DIVISIONS_PROGRESS_UI