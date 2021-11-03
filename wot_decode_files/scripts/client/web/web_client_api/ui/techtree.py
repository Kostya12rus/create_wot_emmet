# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/techtree.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from helpers import dependency
from gui.shared import event_dispatcher, events
from skeletons.gui.shared import IItemsCache
from web.web_client_api import W2CSchema, w2c, Field

class _OpenTechTreeSchema(W2CSchema):
    vehicle_id = Field(required=True, type=int)


class TechTreeTabWebApiMixin(object):
    itemsCache = dependency.descriptor(IItemsCache)

    @w2c(_OpenTechTreeSchema, 'tech_tree')
    def openTechTree(self, cmd):
        event_dispatcher.showTechTree(cmd.vehicle_id)

    @w2c(_OpenTechTreeSchema, 'research')
    def openResearch(self, cmd):
        vehicle = self.itemsCache.items.getStockVehicle(cmd.vehicle_id)
        exitEvent = events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_TECHTREE), ctx={'nation': vehicle.nationName})
        event_dispatcher.showResearchView(cmd.vehicle_id, exitEvent=exitEvent)