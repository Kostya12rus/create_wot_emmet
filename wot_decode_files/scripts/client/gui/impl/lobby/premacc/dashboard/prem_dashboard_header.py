# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/premacc/dashboard/prem_dashboard_header.py
import time, typing, logging, BigWorld
from async import async, await
from account_helpers import account_completion
from constants import RENEWABLE_SUBSCRIPTION_CONFIG
from frameworks.wulf import ViewSettings, ViewStatus
from gui import GUI_SETTINGS
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.clans.clan_helpers import getStrongholdClanCardUrl
from gui.clans.settings import getClanRoleName
from gui.goodies.goodie_items import MAX_ACTIVE_BOOSTERS_COUNT
from gui.impl.gen.view_models.views.lobby.subscription.subscription_card_model import SubscriptionCardState
from gui.impl.lobby.subscription.wot_plus_tooltip import WotPlusTooltip
from gui.platform.wgnp.controller import isEmailConfirmationNeeded, getEmail, isEmailAddingNeeded
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.premacc.dashboard.prem_dashboard_header_model import PremDashboardHeaderModel
from gui.impl.gen.view_models.views.lobby.premacc.dashboard.prem_dashboard_header_reserve_model import PremDashboardHeaderReserveModel
from gui.impl.gen.view_models.views.lobby.premacc.dashboard.prem_dashboard_header_tooltips import PremDashboardHeaderTooltips
from gui.impl.lobby.account_completion.tooltips.hangar_tooltip_view import HangarTooltipView
from gui.impl.lobby.tooltips.clans import ClanShortInfoTooltipContent
from gui.impl.pub import ViewImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared import event_dispatcher
from gui.shared.event_dispatcher import showStrongholds, showAddEmailOverlay, showConfirmEmailOverlay, showWotPlusInfoPage
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IBadgesController, IBoostersController, IExternalLinksController
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from skeletons.gui.web import IWebController
from skeletons.gui.platform.wgnp_controller import IWGNPRequestController
if typing.TYPE_CHECKING:
    from gui.clans.clan_account_profile import ClanAccountProfile
_logger = logging.getLogger(__name__)

class PremDashboardHeader(ViewImpl):
    __slots__ = ('__notConfirmedEmail', '_renewableSub')
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __webCtrl = dependency.descriptor(IWebController)
    __badgesController = dependency.descriptor(IBadgesController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __goodiesCache = dependency.descriptor(IGoodiesCache)
    __boosters = dependency.descriptor(IBoostersController)
    __externalLinks = dependency.descriptor(IExternalLinksController)
    wgnpController = dependency.descriptor(IWGNPRequestController)
    __MAX_VIEWABLE_CLAN_RESERVES_COUNT = 2
    __TOOLTIPS_MAPPING = {PremDashboardHeaderTooltips.TOOLTIP_PERSONAL_RESERVE: TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO, 
       PremDashboardHeaderTooltips.TOOLTIP_CLAN_RESERVE: TOOLTIPS_CONSTANTS.CLAN_RESERVE_INFO}

    def __init__(self):
        settings = ViewSettings(R.views.lobby.premacc.dashboard.prem_dashboard_header.PremDashboardHeader())
        settings.model = PremDashboardHeaderModel()
        super(PremDashboardHeader, self).__init__(settings)
        self.__notConfirmedEmail = ''
        self._renewableSub = BigWorld.player().renewableSubscription

    @property
    def viewModel(self):
        return super(PremDashboardHeader, self).getViewModel()

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipData = self.__getTooltipData(event)
            if tooltipData is None:
                return
            window = backport.BackportTooltipWindow(tooltipData, self.getParentWindow())
            window.load()
            return window
        else:
            return super(PremDashboardHeader, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.tooltips.clans.ClanShortInfoTooltipContent():
            return ClanShortInfoTooltipContent()
        if contentID == R.views.lobby.account_completion.tooltips.HangarTooltip():
            _logger.debug('Show not confirmed email: %s tooltip.', self.__notConfirmedEmail)
            return HangarTooltipView(self.__notConfirmedEmail)
        if event.contentID == R.views.lobby.subscription.WotPlusTooltip():
            return WotPlusTooltip()
        return super(PremDashboardHeader, self).createToolTipContent(event=event, contentID=contentID)

    def _initialize(self, *args, **kwargs):
        super(PremDashboardHeader, self)._initialize(*args, **kwargs)
        self.__initListeners()
        self.viewModel.onShowBadges += self.__onShowBadges
        self.viewModel.personalReserves.onUserItemClicked += self.__onPersonalReserveClick
        self.viewModel.clanReserves.onUserItemClicked += self.__onClanReserveClick
        self.viewModel.onEmailButtonClicked += self.__onEmailButtonClicked
        self.viewModel.subscriptionCard.onCardClick += self.__onSubscriptionClick
        self.viewModel.subscriptionCard.onInfoButtonClik += self.__onSubscriptionInfoClick
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        self._renewableSub.onRenewableSubscriptionDataChanged += self._onWotPlusDataChanged
        with self.viewModel.transaction() as (model):
            userNameModel = model.userName
            userNameModel.setUserName(BigWorld.player().name)
            userNameModel.setIsTeamKiller(self.__itemsCache.items.stats.isTeamKiller)
            self.__updateClanInfo(model)
            self.__updateSubscriptionCard(model)
            self.__buildPersonalReservesList(model=model)
            self.__updateBadges(model=model)
            self.__askEmailStatus()

    def _finalize(self):
        super(PremDashboardHeader, self)._finalize()
        self.viewModel.onShowBadges -= self.__onShowBadges
        self.viewModel.personalReserves.onUserItemClicked -= self.__onPersonalReserveClick
        self.viewModel.clanReserves.onUserItemClicked -= self.__onClanReserveClick
        self.viewModel.onEmailButtonClicked -= self.__onEmailButtonClicked
        self.viewModel.subscriptionCard.onCardClick -= self.__onSubscriptionClick
        self.viewModel.subscriptionCard.onInfoButtonClik -= self.__onSubscriptionInfoClick
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        self._renewableSub.onRenewableSubscriptionDataChanged -= self._onWotPlusDataChanged
        self.__clearListeners()

    def _onWotPlusDataChanged(self, diff):
        with self.viewModel.transaction() as (model):
            self.__updateSubscriptionCard(model)

    def __initListeners(self):
        g_clientUpdateManager.addCallbacks({'stats.clanInfo': self.__onClanInfoChanged, 
           'goodies': self.__onGoodiesUpdated, 
           'cache.activeOrders': self.__onClanInfoChanged})
        self.__badgesController.onUpdated += self.__updateBadges
        self.__boosters.onBoosterChangeNotify += self.__onBoosterChangeNotify
        self.__boosters.onReserveTimerTick += self.__buildClanReservesList
        self.wgnpController.onEmailConfirmed += self.__setEmailConfirmed
        self.wgnpController.onEmailAdded += self.__setEmailActionNeeded
        self.wgnpController.onEmailAddNeeded += self.__setEmailActionNeeded

    def __clearListeners(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__badgesController.onUpdated -= self.__updateBadges
        self.__boosters.onBoosterChangeNotify -= self.__onBoosterChangeNotify
        self.__boosters.onReserveTimerTick -= self.__buildClanReservesList
        self.wgnpController.onEmailConfirmed -= self.__setEmailConfirmed
        self.wgnpController.onEmailAdded -= self.__setEmailActionNeeded
        self.wgnpController.onEmailAddNeeded -= self.__setEmailActionNeeded

    def __onServerSettingsChange(self, diff):
        if RENEWABLE_SUBSCRIPTION_CONFIG in diff:
            with self.viewModel.transaction() as (model):
                self.__updateSubscriptionCard(model)

    def __onClanInfoChanged(self, _):
        self.__updateClanInfo(self.viewModel)

    def __onGoodiesUpdated(self, *_):
        self.__buildPersonalReservesList()
        self.__buildClanReservesList()

    def __onBoosterChangeNotify(self, *_):
        self.__buildPersonalReservesList()

    def __updateSubscriptionCard(self, model):
        isWotPlusEnabled = self.__lobbyContext.getServerSettings().isRenewableSubEnabled()
        isWotPlusNSEnabled = self.__lobbyContext.getServerSettings().isWotPlusNewSubscriptionEnabled()
        hasWotPlusActive = self._renewableSub.isEnabled()
        showSubscriptionCard = isWotPlusEnabled and (hasWotPlusActive or isWotPlusNSEnabled)
        model.setIsSubscriptionEnable(showSubscriptionCard)
        if showSubscriptionCard:
            state = SubscriptionCardState.AVAILABLE
            if hasWotPlusActive:
                state = SubscriptionCardState.ACTIVE
                expirationTime = self._renewableSub.getExpiryTime()
                model.subscriptionCard.setNextCharge(time.strftime('%d.%m', time.localtime(expirationTime)))
            model.subscriptionCard.setState(state)

    def __updateClanInfo(self, model):
        clanProfile = self.__getAccountProfile()
        isInClan = clanProfile.isInClan()
        model.setIsInClan(isInClan)
        if isInClan:
            clanInfoModel = model.clanInfo
            clanAbbrev = clanProfile.getClanAbbrev()
            model.userName.setClanAbbrev(clanAbbrev)
            clanInfoModel.setClanAbbrev(clanAbbrev)
            clanInfoModel.setRoleInClan(getClanRoleName(clanProfile.getRole()) or '')
            self.__buildClanReservesList(model=model)

    @replaceNoneKwargsModel
    def __buildPersonalReservesList(self, _=None, model=None):
        listModel = model.personalReserves
        listModel.clearItems()
        activeBoosters = self.__goodiesCache.getBoosters(criteria=REQ_CRITERIA.BOOSTER.ACTIVE)
        activeBoostersList = sorted(activeBoosters.values(), key=lambda b: b.getUsageLeftTime(), reverse=True)
        for idx in range(MAX_ACTIVE_BOOSTERS_COUNT):
            itemModel = self.__makeReserveModel(activeBoostersList, idx)
            listModel.addViewModel(itemModel)

        listModel.invalidate()

    @replaceNoneKwargsModel
    def __buildClanReservesList(self, _=None, model=None):
        clanProfile = self.__getAccountProfile()
        mayActivate = clanProfile.getMyClanPermissions().canActivateReserves()
        activeReserves = sorted(self.__goodiesCache.getClanReserves().values(), key=lambda r: r.finishTime)
        showSection = mayActivate or activeReserves
        model.setHasClanReserves(bool(showSection))
        if showSection:
            listModel = model.clanReserves
            listItems = listModel.getItems()
            if listItems:
                listItems.clear()
            if mayActivate:
                slotsCount = self.__MAX_VIEWABLE_CLAN_RESERVES_COUNT
            else:
                slotsCount = min(len(activeReserves), self.__MAX_VIEWABLE_CLAN_RESERVES_COUNT)
            for idx in range(slotsCount):
                itemModel = self.__makeReserveModel(activeReserves, idx)
                listModel.addViewModel(itemModel)

            listModel.invalidate()

    def __getAccountProfile(self):
        return self.__webCtrl.getAccountProfile()

    def __getTooltipData(self, event):
        tooltipType = event.getArgument('tooltipType')
        tooltipAlias = self.__TOOLTIPS_MAPPING.get(tooltipType)
        if tooltipAlias:
            reserveId = event.getArgument('id')
            return backport.createTooltipData(isSpecial=True, specialAlias=tooltipAlias, specialArgs=(
             reserveId,))

    @replaceNoneKwargsModel
    def __updateBadges(self, model=None):
        prefixBadge = self.__badgesController.getPrefix()
        self.__setBadge(model.setPrefixBadgeId, prefixBadge)
        self.__setBadge(model.setSuffixBadgeId, self.__badgesController.getSuffix())
        if prefixBadge is not None:
            model.setIsDynamicBadge(prefixBadge.hasDynamicContent())
            model.setBadgeContent(prefixBadge.getDynamicContent() or '')
        else:
            model.setIsDynamicBadge(False)
            model.setBadgeContent('')
        return

    @replaceNoneKwargsModel
    def __setEmailConfirmed(self, model=None):
        model.setEmailButtonLabel(R.invalid())
        model.setIsWarningIconVisible(False)
        model.setShowEmailActionTooltip(False)
        self.__notConfirmedEmail = ''
        _logger.debug('User email confirmed.')

    @replaceNoneKwargsModel
    def __setEmailActionNeeded(self, notConfirmedEmail='', model=None):
        model.setIsWarningIconVisible(True)
        model.setShowEmailActionTooltip(True)
        if notConfirmedEmail:
            model.setEmailButtonLabel(R.strings.badge.badgesPage.accountCompletion.button.confirmEmail())
        else:
            model.setEmailButtonLabel(R.strings.badge.badgesPage.accountCompletion.button.provideEmail())
        self.__notConfirmedEmail = notConfirmedEmail
        _logger.debug('User email: %s action needed.', notConfirmedEmail)

    @async
    def __askEmailStatus(self):
        if not account_completion.isEnabled():
            _logger.debug('Account completion disabled.')
            return
        else:
            _logger.debug('Sending email status request.')
            response = yield await(self.wgnpController.getEmailStatus())
            destroyed = self.viewStatus in (ViewStatus.DESTROYED, ViewStatus.DESTROYING)
            if not response.isSuccess() or destroyed or self.viewModel is None:
                _logger.warning('Can not get account email status.')
                return
            if isEmailAddingNeeded(response):
                self.__setEmailActionNeeded(notConfirmedEmail='')
            elif isEmailConfirmationNeeded(response):
                self.__setEmailActionNeeded(notConfirmedEmail=getEmail(response))
            else:
                self.__setEmailConfirmed()
            return

    def __onEmailButtonClicked(self):
        label = self.viewModel.getEmailButtonLabel()
        if label == R.strings.badge.badgesPage.accountCompletion.button.confirmEmail():
            _logger.debug('Show email confirmation overlay with email=%s.', self.__notConfirmedEmail)
            showConfirmEmailOverlay(email=self.__notConfirmedEmail)
        elif label == R.strings.badge.badgesPage.accountCompletion.button.provideEmail():
            _logger.debug('Show add email overlay.')
            showAddEmailOverlay()
        else:
            _logger.warning('Unknown email button label: %s. Action skipped.', label)

    @staticmethod
    def __setBadge(setter, badge):
        setter(badge.getIconPostfix() if badge is not None and badge.isSelected else '')
        return

    @staticmethod
    def __onShowBadges():
        event_dispatcher.showBadges(backViewName=backport.text(R.strings.badge.badgesPage.header.backBtn.descrLabel()))

    @staticmethod
    def __onPersonalReserveClick(_):
        event_dispatcher.showStorage(defaultSection=STORAGE_CONSTANTS.PERSONAL_RESERVES)

    @staticmethod
    def __onClanReserveClick(_):
        showStrongholds(getStrongholdClanCardUrl())

    @staticmethod
    def __makeReserveModel(reserves, idx):
        itemModel = PremDashboardHeaderReserveModel()
        if idx < len(reserves):
            booster = reserves[idx]
            itemModel.setId(booster.boosterID)
            itemModel.setProgress(booster.getCooldownAsPercent())
            itemModel.setTimeleft(booster.getUsageLeftTime())
            itemModel.setIconId(booster.boosterGuiType)
        return itemModel

    def __onSubscriptionClick(self):
        url = GUI_SETTINGS.wotPlusManageSubscriptionUrl
        self.__externalLinks.open(url)

    def __onSubscriptionInfoClick(self):
        showWotPlusInfoPage()