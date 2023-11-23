# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/dialogs/price_cards_content/recruit_new_tankman_price_list.py
import typing
from frameworks.wulf import ViewSettings, Array
from gui.impl.auxiliary.tankman_operations import packRecruit
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_list_model import PriceListModel
from gui.impl.lobby.crew.dialogs.price_cards_content.base_price_list import BasePriceList
from gui.shared.gui_items.gui_item_economics import ItemPrice
from gui.shared.money import Currency, Money
if typing.TYPE_CHECKING:
    from gui.shared.utils.requesters import ShopRequester
    from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_card_model import PriceCardModel

class RecruitNewTankmanPriceList(BasePriceList):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.crew.widgets.PriceList())
        settings.model = PriceListModel()
        super(RecruitNewTankmanPriceList, self).__init__(settings)

    @property
    def _priceListPacker(self):
        return packRecruit

    def _fillPrices(self):
        shopRequester = self._itemsCache.items.shop
        tankmanCost = shopRequester.tankmanCost
        defaultTankmanCost = shopRequester.defaults.tankmanCost
        self._priceData = []
        for idx, cost in enumerate(tankmanCost):
            defCost = defaultTankmanCost[idx]
            itemPrice = ItemPrice(price=Money(credits=cost.get(Currency.CREDITS, 0), gold=cost.get(Currency.GOLD, 0)), defPrice=Money(credits=defCost.get(Currency.CREDITS, 0), gold=defCost.get(Currency.GOLD, 0)))
            self._priceData.append((itemPrice, cost, idx))

    def _onTankmanChanged(self, _):
        pass