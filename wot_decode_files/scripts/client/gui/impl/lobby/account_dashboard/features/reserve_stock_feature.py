# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_dashboard/features/reserve_stock_feature.py
import typing
from constants import PremiumConfigs, PREMIUM_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl.lobby.account_dashboard.features.base import FeatureItem
from gui.impl.lobby.premacc.premacc_helpers import PiggyBankConstants, getOpenTimeHelper
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared.event_dispatcher import showPiggyBankView
from helpers import dependency
from skeletons.gui.game_control import IGameSessionController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.account_dashboard.reserve_stock_model import ReserveStockModel

class ReserveStockFeature(FeatureItem):
    _itemsCache = dependency.descriptor(IItemsCache)
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _gameSession = dependency.descriptor(IGameSessionController)

    def initialize(self, *args, **kwargs):
        super(ReserveStockFeature, self).initialize(*args, **kwargs)
        g_clientUpdateManager.addCallbacks({PiggyBankConstants.PIGGY_BANK: self._onPiggyBankChanged, 
           PiggyBankConstants.PIGGY_BANK_CREDITS: self._updateCredits, 
           PiggyBankConstants.PIGGY_BANK_SMASH_TIMESTAMP_CREDITS: self._updateLastSmashTimestamp})
        self._gameSession.onPremiumNotify += self._updatePrem
        self._lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        self._viewModel.reserveStock.onClick += self.__onClick

    def finalize(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self._gameSession.onPremiumNotify -= self._updatePrem
        self._lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        self._viewModel.reserveStock.onClick -= self.__onClick
        super(ReserveStockFeature, self).finalize()

    def _fillModel(self, model):
        self._update(model=model)

    def _updateCredits(self, credits_=None):
        self._update(credits_=credits_)

    def _updatePrem(self, *args):
        self._update()

    def _updateLastSmashTimestamp(self, _):
        self._update()

    def _onPiggyBankChanged(self, _):
        self._update()

    def __onServerSettingsChange(self, diff):
        if PremiumConfigs.PIGGYBANK in diff:
            self._update()

    @replaceNoneKwargsModel
    def _update(self, credits_=None, model=None):
        submodel = model.reserveStock
        config = self._lobbyContext.getServerSettings().getPiggyBankConfig()
        data = self._itemsCache.items.stats.piggyBank
        submodel.setIsEnabled(config.get('enabled', False))
        submodel.setCreditCurrentAmount(credits_ or data.get('credits', 0))
        submodel.setCreditMaxAmount(config.get('creditsThreshold', PiggyBankConstants.MAX_AMOUNT))
        submodel.setIsPremiumActive(self.__isTankPremiumActive())
        submodel.setOpeningSoonThreshold(config.get('openSoonThreshold', PiggyBankConstants.OPEN_SOON_THRESHOLD_DEFAULT))
        submodel.setOpeningTime(getOpenTimeHelper(config, data))

    def __onClick(self):
        if self._lobbyContext.getServerSettings().getPiggyBankConfig().get('enabled', False):
            showPiggyBankView()

    def __isTankPremiumActive(self):
        return self._itemsCache.items.stats.isActivePremium(PREMIUM_TYPE.PLUS)