# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/ranked/ranked_calendar_day_extended_tooltip.py
from datetime import datetime
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.tooltips import formatters
from gui.shared.tooltips.ranked.ranked_calendar_day_tooltip import RankedCalendarDayTooltip
from gui.Scaleform.daapi.view.lobby.formatters.tooltips import packCalendarBlock
from helpers import dependency, time_utils
from skeletons.gui.game_control import IRankedBattlesController
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES
_TOOLTIP_MIN_WIDTH = 200

class RankedCalendarDayExtendedTooltip(RankedCalendarDayTooltip):
    rankedController = dependency.descriptor(IRankedBattlesController)

    def _packBlocks(self, selectedTime):
        items = []
        if self.__isSeasonEnded(selectedTime):
            return items
        blocks = []
        currentSeason = self.rankedController.getCurrentSeason()
        if currentSeason:
            daysLeft = int((currentSeason.getEndDate() - time_utils.getServerUTCTime()) / time_utils.ONE_DAY)
            seasonName = currentSeason.getUserName() or currentSeason.getNumber()
            blocks.append(self.__packTimeLeftBlock(seasonName, daysLeft))
        blocks.append(self._packHeaderBlock())
        blocks += self.__packCalendarBlock(selectedTime)
        items.append(formatters.packBuildUpBlockData(blocks, 13))
        return items

    def __packTimeLeftBlock(self, name, daysLeft):
        return formatters.packTextBlockData(text=text_styles.stats(backport.text(R.strings.ranked_battles.calendarDay.timeLeft(), seasonName=name, days=daysLeft)), blockWidth=_TOOLTIP_MIN_WIDTH)

    def __isSeasonEnded(self, selectedTime):
        if selectedTime is None:
            selectedTime = time_utils.getCurrentLocalServerTimestamp()
        seasonEnd = None
        if self.rankedController.getCurrentSeason():
            seasonEnd = self.rankedController.getCurrentSeason().getEndDate()
            seasonEnd = datetime.fromtimestamp(seasonEnd).date()
        return datetime.fromtimestamp(selectedTime).date() > seasonEnd

    def __packCalendarBlock(self, selectedTime):
        return packCalendarBlock(self.rankedController, selectedTime, SELECTOR_BATTLE_TYPES.RANKED)