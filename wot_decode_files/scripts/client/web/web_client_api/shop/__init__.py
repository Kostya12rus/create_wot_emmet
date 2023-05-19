# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/shop/__init__.py
from web.web_client_api import w2capi
from web.web_client_api.shop.actions import ActionsWebApiMixin
from web.web_client_api.shop.boosters import BoostersInfoWebApiMixin
from web.web_client_api.shop.renewable_subscription import RenewableSubWebApiMixin
from web.web_client_api.shop.stats import BalanceWebApiMixin
from web.web_client_api.shop.stock import ItemsWebApiMixin
from web.web_client_api.shop.telecom_rentals import TelecomRentalsWebApiMixin
from web.web_client_api.shop.trade import TradeWebApiMixin
from web.web_client_api.shop.unified_trade_in import UnifiedTradeInWebApiMixin

@w2capi(name='shop', key='action')
class ShopWebApi(ActionsWebApiMixin, BalanceWebApiMixin, ItemsWebApiMixin, TradeWebApiMixin, UnifiedTradeInWebApiMixin, BoostersInfoWebApiMixin, RenewableSubWebApiMixin, TelecomRentalsWebApiMixin):
    pass