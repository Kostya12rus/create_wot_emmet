# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/dialogs/price_cards_content/base_price_list.py
import typing, Event
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.auxiliary.tankman_operations import packPriceList
from gui.impl.backport.backport_tooltip import createBackportTooltipContent
from gui.impl.gen.resources import R
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_card_model import PriceCardModel, CardState
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_list_model import PriceListModel
from gui.impl.pub import ViewImpl
from gui.shared.items_cache import CACHE_SYNC_REASON
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array

class BasePriceList(ViewImpl):
    __slots__ = ('_selectedCardIndex', '_priceData', 'onPriceChange')
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, settings):
        self._selectedCardIndex = None
        self._priceData = []
        self._fillPrices()
        self.onPriceChange = Event.Event()
        super(BasePriceList, self).__init__(settings)
        return

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.dialogs.common.DialogTemplateGenericTooltip():
            index = int(event.getArgument('index'))
            itemPrice, _, _ = self._getPriceData(index)
            if not itemPrice:
                return
            if itemPrice.isActionPrice():
                specialAlias = (
                 None, None,
                 itemPrice.price.toMoneyTuple(),
                 itemPrice.defPrice.toMoneyTuple(),
                 True, False, None, True)
                return createBackportTooltipContent(specialAlias=TOOLTIPS_CONSTANTS.ACTION_PRICE, specialArgs=specialAlias)
            shortage = self._itemsCache.items.stats.money.getShortage(itemPrice.price)
            if bool(shortage):
                currency = shortage.getCurrency()
                return createBackportTooltipContent(TOOLTIPS_CONSTANTS.NOT_ENOUGH_MONEY, (
                 shortage.get(currency), currency))
        return super(BasePriceList, self).createToolTipContent(event, contentID)

    @property
    def viewModel(self):
        return self.getViewModel()

    @property
    def selectedPriceData(self):
        return self._getPriceData(self._selectedCardIndex)

    @property
    def _priceListPacker(self):
        return packPriceList

    def _selectCard(self, vm, index=None):
        if self._selectedCardIndex is not None:
            self._getCard(vm, self._selectedCardIndex).setCardState(CardState.DEFAULT)
        if index is not None:
            self._getCard(vm, index).setCardState(CardState.SELECTED)
        self._selectedCardIndex = index
        self.onPriceChange(self._selectedCardIndex)
        return

    def _fillPrices(self):
        pass

    def _onLoading(self, *args, **kwargs):
        super(BasePriceList, self)._onLoading(*args, **kwargs)
        self._updateViewModel()

    @staticmethod
    def _getCard(vm, index):
        return vm.getCardsList().getValue(index)

    def _getPriceData(self, index):
        if index is not None and len(self._priceData) >= index + 1:
            return self._priceData[index]
        else:
            return (None, None, None)

    def _getEvents(self):
        return (
         (
          self.viewModel.onCardClick, self._onCardClick),
         (
          self._itemsCache.onSyncCompleted, self._onCacheResync))

    def _getCallbacks(self):
        return (
         (
          'stats.gold', self._onGoldUpdate),
         (
          'stats.credits', self._onCreditsUpdate),
         (
          'inventory.8.compDescr', self._onTankmanChanged),
         (
          'cache.mayConsumeWalletResources', self._onConsumeWalletUpdate))

    def _updateViewModel(self):
        with self.viewModel.transaction() as (vm):
            self._fillViewModel(vm)

    def _fillViewModel(self, vm):
        cardList = vm.getCardsList()
        cardList.clear()
        self._priceListPacker(cardList, self._priceData)
        if self._selectedCardIndex is not None:
            card = cardList.getValue(self._selectedCardIndex)
            cardIndex = None if card.getCardState() == CardState.DISABLED else self._selectedCardIndex
            self._selectCard(vm, cardIndex)
        cardList.invalidate()
        return

    def _onTankmanChanged(self, data):
        self._updateViewModel()

    def _onConsumeWalletUpdate(self, *_):
        self._updateViewModel()

    def _onCreditsUpdate(self, *_):
        self._updateViewModel()

    def _onGoldUpdate(self, *_):
        self._updateViewModel()

    def _onCacheResync(self, reason, _):
        if reason in (CACHE_SYNC_REASON.SHOP_RESYNC, CACHE_SYNC_REASON.DOSSIER_RESYNC):
            self._fillPrices()
            self._updateViewModel()

    def _onCardClick(self, args):
        with self.viewModel.transaction() as (vm):
            self._selectCard(vm, int(args.get('index', 0)))