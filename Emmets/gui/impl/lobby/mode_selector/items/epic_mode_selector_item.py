# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/items/epic_mode_selector_item.py
import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_columns import ModeSelectorColumns
from gui.impl.lobby.mode_selector.items import setBattlePassState
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID
from gui.shared.formatters import time_formatters
from gui.shared.formatters.ranges import toRomanRangeString
from helpers import dependency, time_utils, int2roman
from skeletons.gui.game_control import IEpicBattleMetaGameController
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import BattlePassState
from skeletons.gui.server_events import IEventsCache
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel

class EpicModeSelectorItem(ModeSelectorLegacyItem):
    __slots__ = ()
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.EPIC_BATTLE
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)
    __eventsCache = dependency.descriptor(IEventsCache)

    @property
    def preferredColumn(self):
        if self.__eventsCache.isEventEnabled():
            return ModeSelectorColumns.COLUMN_2
        return self._preferredColumn

    def _getIsDisabled(self):
        return not self.__epicController.isEnabled()

    def _onInitializing(self):
        super(EpicModeSelectorItem, self)._onInitializing()
        self.__epicController.onPrimeTimeStatusUpdated += self.__onEpicUpdate
        self.__epicController.onUpdated += self.__onEpicUpdate
        self.__fillViewModel()

    def _onDisposing(self):
        self.__epicController.onPrimeTimeStatusUpdated -= self.__onEpicUpdate
        self.__epicController.onUpdated -= self.__onEpicUpdate
        super(EpicModeSelectorItem, self)._onDisposing()

    def __onEpicUpdate(self, *_):
        self.__fillViewModel()

    def __fillViewModel(self):
        with self.viewModel.transaction() as (vm):
            self.__resetViewModel(vm)
            currentSeason = self.__epicController.getCurrentSeason()
            nextSeason = self.__epicController.getNextSeason()
            season = currentSeason or nextSeason
            currentTime = time_utils.getCurrentLocalServerTimestamp()
            vm.setConditions(backport.text(R.strings.mode_selector.mode.epicBattle.condition(), levels=toRomanRangeString(self.__epicController.getValidVehicleLevels())))
            vm.setDescription(backport.text(R.strings.mode_selector.mode.epicBattle.description()))
            if season is None:
                return
            if season.hasActiveCycle(currentTime):
                vm.setStatusActive(backport.text(R.strings.mode_selector.mode.epicBattle.seasonActive(), cycle=int2roman(currentSeason.getCycleInfo().getEpicCycleNumber())))
                self._addReward(ModeSelectorRewardID.CREDITS)
                self._addReward(ModeSelectorRewardID.EXPERIENCE)
                timeLeftStr = ''
                cycleInfo = season.getCycleInfo()
                if cycleInfo is not None:
                    timeLeftStr = time_formatters.getTillTimeByResource(cycleInfo.endDate - currentTime, R.strings.menu.Time.timeLeftShort, removeLeadingZeros=True)
                vm.setTimeLeft(timeLeftStr)
            else:
                cycleInfo = season.getNextByTimeCycle(currentTime)
                if cycleInfo is not None:
                    if cycleInfo.announceOnly:
                        vm.setStatusNotActive(backport.text(R.strings.mode_selector.mode.epicBattle.cycleSoon(), cycle=int2roman(cycleInfo.getEpicCycleNumber())))
                    else:
                        vm.setStatusNotActive(backport.text(R.strings.mode_selector.mode.epicBattle.cycleNext(), cycle=int2roman(cycleInfo.getEpicCycleNumber()), date=backport.getShortDateFormat(cycleInfo.startDate)))
                    self.viewModel.setBattlePassState(BattlePassState.NONE)
                else:
                    vm.setStatusNotActive(backport.text(R.strings.mode_selector.mode.epicBattle.seasonEnd()))
        setBattlePassState(self.viewModel)
        return

    @staticmethod
    def __resetViewModel(vm):
        vm.setTimeLeft('')
        vm.setStatusActive('')
        vm.setStatusNotActive('')
        vm.getRewardList().clear()