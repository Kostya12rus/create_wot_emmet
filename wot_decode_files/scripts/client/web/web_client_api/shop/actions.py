# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/shop/actions.py
from gui.Scaleform.daapi.view.lobby.store.actions_formatters import getAllActionsInfoIterator
from helpers import dependency
from web.web_client_api import w2c, W2CSchema
from skeletons.gui.server_events import IEventsCache
from web.web_client_api.shop import formatters

def _filterActions(act):
    return act.isAvailable().isValid


class ActionsWebApiMixin(object):
    eventsCache = dependency.descriptor(IEventsCache)

    @w2c(W2CSchema, 'get_actions')
    def getActions(self, _):
        actions = self.eventsCache.getActions(filterFunc=_filterActions).values()
        entities = self.eventsCache.getActionEntities()
        actionsInfo = getAllActionsInfoIterator(actions, entities) if actions else []
        fmt = formatters.makeActionFormatter().format
        return [ fmt(actionInfo) for actionInfo in actionsInfo ]