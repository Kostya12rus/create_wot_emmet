# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/view_helpers.py
import typing
from gui.shared.missions.packers.bonus import getDefaultBonusPacker
if typing.TYPE_CHECKING:
    from typing import TypeVar
    from frameworks.wulf import Array
    from gui.server_events.bonuses import SimpleBonus
    from gui.shared.missions.packers.bonus import BonusUIPacker
    from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
    BonusModelType = TypeVar('BonusModelType', bound=BonusModel)

def packBonusModelAndTooltipData(bonuses, bonusModelsList, tooltipData=None, packer=None):
    packer = packer or getDefaultBonusPacker()
    tooltipIndex = 0 if tooltipData is None else len(tooltipData)
    for bonus in (b for b in bonuses if b.isShowInGUI()):
        bonusList = packer.pack(bonus)
        withTooltips = bonusList and tooltipData is not None
        bTooltipList = packer.getToolTip(bonus) if withTooltips else []
        bContentIdList = packer.getContentId(bonus) if withTooltips else []
        for bIndex, bModel in enumerate(bonusList):
            bModel.setIndex(bIndex)
            tooltipIndex = _packBonusTooltip(bModel, bIndex, bTooltipList, bContentIdList, tooltipData, tooltipIndex)
            bonusModelsList.addViewModel(bModel)

    return


def _packBonusTooltip(bonusModel, bonusIndex, bonusTooltipList, bonusContentIdList, tooltipData, tooltipIndex):
    if tooltipData is None or not bonusTooltipList and not bonusContentIdList:
        return tooltipIndex
    tooltipIdx = str(tooltipIndex)
    bonusModel.setTooltipId(tooltipIdx)
    if bonusTooltipList:
        tooltipData[tooltipIdx] = bonusTooltipList[bonusIndex]
    if bonusContentIdList:
        bonusModel.setTooltipContentId(str(bonusContentIdList[bonusIndex]))
    return tooltipIndex + 1