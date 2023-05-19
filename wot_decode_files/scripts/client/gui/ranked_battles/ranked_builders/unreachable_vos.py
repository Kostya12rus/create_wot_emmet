# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/ranked_battles/ranked_builders/unreachable_vos.py
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from helpers import int2roman
from main_page_vos import getRankedMainSeasonOnHeader

def getUnreachableVO(season, minLevel, maxLevel, isAvailableForBuy, isAvailableForRestore):
    levelsStr = __formatUnreachableLevels(minLevel, maxLevel)
    centerText = R.strings.ranked_battles.rankedBattlesUnreachableView.vehicleUnavailable
    if isAvailableForBuy:
        centerText = R.strings.ranked_battles.rankedBattlesUnreachableView.vehicleAvailableForBuy
    elif isAvailableForRestore:
        centerText = R.strings.ranked_battles.rankedBattlesUnreachableView.vehicleAvailableForRestore
    return {'bottomRules': __formatBottomItems(), 'header': getRankedMainSeasonOnHeader(season, None), 
       'centerText': text_styles.vehicleStatusCriticalText(backport.text(centerText(), levels=levelsStr)), 
       'bottomText': text_styles.highTitle(backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottomText(), levels=levelsStr)), 
       'closeBtnLabel': backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.closeBtnLabel()), 
       'closeBtnTooltip': '', 
       'bgImage': backport.image(R.images.gui.maps.icons.rankedBattles.bg.main()), 
       'centerImg': backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.ranked_battle_locked_sm()), 
       'centerImgBig': backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.ranked_battle_locked_big())}


def __formatBottomItems():
    return [
     {'tooltip': '', 
        'image': backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.icon_prem()), 
        'description': text_styles.main(backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottom.premium(), premiumType=backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottom.premium.plus())))},
     {'tooltip': '', 
        'image': backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.icon_ranks_task_200x100()), 
        'description': text_styles.main(backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottom.missions()))},
     {'tooltip': '', 
        'image': backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.icon_reserves()), 
        'description': text_styles.main(backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottom.reserves()))}]


def __formatUnreachableLevels(minLevel, maxLevel):
    if minLevel == maxLevel:
        return int2roman(minLevel)
    return ('{0}-{1}').format(int2roman(minLevel), int2roman(maxLevel))