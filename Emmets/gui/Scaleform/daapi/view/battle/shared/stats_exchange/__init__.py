# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/stats_exchange/__init__.py
import weakref
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import player
from gui.Scaleform.daapi.view.battle.shared.stats_exchange.stats_ctrl import BattleStatisticsDataController
__all__ = ('BattleStatisticsDataController', 'createExchangeBroker')

def createExchangeBroker(exchangeCtx):
    proxy = weakref.proxy(exchangeCtx)
    exchangeBroker = broker.ExchangeBroker(exchangeCtx)
    exchangeBroker.setPlayerStatusExchange(player.PlayerStatusComponent())
    exchangeBroker.setUsersTagsExchange(player.UsersTagsListExchangeData(proxy))
    exchangeBroker.setInvitationsExchange(player.InvitationsExchangeBlock())
    return exchangeBroker