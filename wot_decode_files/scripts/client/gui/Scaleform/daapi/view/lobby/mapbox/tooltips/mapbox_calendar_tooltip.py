# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_calendar_tooltip.py
from gui.impl.gen import R
from gui.impl import backport
from gui.Scaleform.daapi.view.lobby.formatters.tooltips import packCalendarBlock
from gui.shared.tooltips import formatters, TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData
from helpers import dependency, time_utils
from skeletons.gui.game_control import IMapboxController
from gui.shared.formatters import text_styles
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES

class MapboxCalendarTooltip(BlocksTooltipData):
    __mapboxCtrl = dependency.descriptor(IMapboxController)

    def __init__(self, context):
        super(MapboxCalendarTooltip, self).__init__(context, TOOLTIP_TYPE.MAPBOX_SELECTOR_INFO)
        self._setWidth(360)

    def _packBlocks(self, *args, **kwargs):
        blocks = super(MapboxCalendarTooltip, self)._packBlocks(args, kwargs)
        blocks.append(formatters.packBuildUpBlockData([
         self.__packHeader(),
         self.__packTimeTableHeaderBlock(),
         formatters.packBuildUpBlockData(packCalendarBlock(self.__mapboxCtrl, time_utils.getCurrentTimestamp(), SELECTOR_BATTLE_TYPES.MAPBOX))]))
        return blocks

    def __packHeader(self):
        return formatters.packTextBlockData(text_styles.highlightText(backport.text(R.strings.mapbox.selector.tooltip.body(), day=self.__getCurrentSeasonDate())), padding=formatters.packPadding(bottom=10))

    def __getCurrentSeasonDate(self):
        currentSeason = self.__mapboxCtrl.getCurrentSeason()
        if currentSeason is not None:
            return self.__getDate(currentSeason.getEndDate())
        else:
            return ''

    def __getDate(self, date):
        timeStamp = time_utils.makeLocalServerTime(date)
        return backport.getShortDateFormat(timeStamp)

    def __packTimeTableHeaderBlock(self):
        return formatters.packImageTextBlockData(title=text_styles.highTitle(backport.text(R.strings.mapbox.selector.tooltip.title())), img=backport.image(R.images.gui.maps.icons.buttons.calendar()), imgPadding=formatters.packPadding(top=5), txtPadding=formatters.packPadding(left=10))