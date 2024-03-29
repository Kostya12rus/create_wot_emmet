# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/subscription/subscription_award_view.py
from helpers.time_utils import makeLocalServerTime
from typing import TYPE_CHECKING
import WWISE
from frameworks.wulf import ViewSettings
from gui.Scaleform.daapi.view.lobby.wot_plus.sound_constants import SOUNDS
from gui.impl import backport
from gui.impl.backport import BackportTooltipWindow
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.subscription.subscription_award_view_model import SubscriptionAwardViewModel
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.server_events.bonuses import GoldBank, IdleCrewXP, ExcludedMap, FreeEquipmentDemounting, WoTPlusExclusiveVehicle, WoTPlusBonus
from gui.shared.event_dispatcher import showWotPlusInfoPage
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap
from helpers import dependency
from skeletons.gui.game_control import IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource, WotPlusKeys
from uilogging.wot_plus.loggers import WotPlusRewardTooltipLogger, WotPlusRewardScreenLogger
if TYPE_CHECKING:
    from typing import Dict, List, Optional
    from gui.impl.backport import TooltipData
    from gui.shared.missions.packers.bonus import BaseBonusUIPacker
    from frameworks.wulf import ViewEvent, Window

class LoggedBackportTooltipWindow(BackportTooltipWindow):
    __slots__ = ('_wotPlusUILogger', )

    def __init__(self, tooltipData, parent, bonusName):
        super(LoggedBackportTooltipWindow, self).__init__(tooltipData, parent)
        self._wotPlusUILogger = WotPlusRewardTooltipLogger(WotPlusKeys.REWARD_SCREEN, bonusName)

    def _initialize(self):
        super(LoggedBackportTooltipWindow, self)._initialize()
        self._wotPlusUILogger.onViewInitialize()

    def _finalize(self):
        super(LoggedBackportTooltipWindow, self)._finalize()
        self._wotPlusUILogger.onViewFinalize()


class SubscriptionAwardView(ViewImpl):
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)
    __slots__ = ('__tooltips', '__bonuses', '_wotPlusUILogger')

    def __init__(self, layoutID, *args, **kwargs):
        settings = ViewSettings(layoutID)
        settings.model = SubscriptionAwardViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(SubscriptionAwardView, self).__init__(settings)
        self.__tooltips = {}
        self.__bonuses = self._getBonuses()
        self._wotPlusUILogger = WotPlusRewardScreenLogger()

    @property
    def viewModel(self):
        return super(SubscriptionAwardView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        self._wotPlusUILogger.onViewInitialize()
        self.viewModel.onCloseButtonClick += self._onClose
        self.viewModel.onInfoButtonClick += self._onInfo

    def _finalize(self):
        self._wotPlusUILogger.onViewFinalize()
        self._wotPlusUILogger.logCloseEvent()
        self.viewModel.onCloseButtonClick -= self._onClose
        self.viewModel.onInfoButtonClick -= self._onInfo
        self._soundsOnClose()

    def _getBonuses(self):
        serverSettings = self._lobbyContext.getServerSettings()
        bonuses = []
        if serverSettings.isWoTPlusExclusiveVehicleEnabled():
            bonuses.append(WoTPlusExclusiveVehicle())
        if serverSettings.isRenewableSubGoldReserveEnabled():
            bonuses.append(GoldBank())
        if serverSettings.isRenewableSubPassiveCrewXPEnabled():
            bonuses.append(IdleCrewXP())
        if serverSettings.isWotPlusExcludedMapEnabled():
            bonuses.append(ExcludedMap())
        if serverSettings.isFreeEquipmentDemountingEnabled():
            bonuses.append(FreeEquipmentDemounting())
        return bonuses

    def _fillViewModel(self):
        with self.getViewModel().transaction() as (model):
            rewardsList = model.getRewards()
            rewardsList.clear()
            rewardsList.reserve(len(self.__bonuses))
            packerMap = getDefaultBonusPackersMap()
            for index, bonus in enumerate(self.__bonuses):
                packer = packerMap.get(bonus.getName())
                if packer:
                    tooltipsData = packer.getToolTip(bonus)
                    for bonusIdx, bonusModel in enumerate(packer.pack(bonus)):
                        bonusModel.setTooltipId(str(index))
                        tooltip = tooltipsData[bonusIdx]
                        rewardsList.addViewModel(bonusModel)
                        self.__tooltips[index] = tooltip

            model.setNextCharge(makeLocalServerTime(self._wotPlusCtrl.getExpiryTime()) or 0)
            rewardsList.invalidate()

    def _onLoading(self, *args, **kwargs):
        self._fillViewModel()
        self._soundsOnOpen()

    def _onClose(self):
        self.destroyWindow()

    def _onInfo(self):
        showWotPlusInfoPage(WotPlusInfoPageSource.REWARD_SCREEN)

    def _soundsOnOpen(self):
        WWISE.WW_eventGlobal(backport.sound(R.sounds.gui_reward_screen_general()))
        WWISE.WW_setState(SOUNDS.OVERLAY_HANGAR_GENERAL, SOUNDS.OVERLAY_HANGAR_GENERAL_ON)

    def _soundsOnClose(self):
        WWISE.WW_setState(SOUNDS.OVERLAY_HANGAR_GENERAL, SOUNDS.OVERLAY_HANGAR_GENERAL_OFF)

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = int(event.getArgument('tooltipId'))
            window = None
            if tooltipId in self.__tooltips and 0 <= tooltipId < len(self.__bonuses):
                bonusName = self.__bonuses[tooltipId].getName()
                window = LoggedBackportTooltipWindow(self.__tooltips[tooltipId], self.getParentWindow(), bonusName)
                window.load()
            return window
        return super(SubscriptionAwardView, self).createToolTip(event)


class SubscriptionAwardWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self):
        super(SubscriptionAwardWindow, self).__init__(content=SubscriptionAwardView(R.views.lobby.subscription.SubscriptionAwardView()))