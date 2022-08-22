# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/shop/boosters.py
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.goodies import IGoodiesCache
from web.web_client_api import w2c, W2CSchema, Field

class _ActiveBoostersSchema(W2CSchema):
    filter_types = Field(required=False, type=list, default=None)


class BoostersInfoWebApiMixin(object):
    __goodiesCache = dependency.descriptor(IGoodiesCache)

    @w2c(_ActiveBoostersSchema, 'get_active_boosters')
    def getActiveBoosters(self, cmd):
        return [ {'id': booster.boosterID, 'type': booster.boosterType, 'time_remaining': booster.getUsageLeftTime(), 'formatted_time_remaining': booster.getUsageLeftTimeStr()} for booster in self.__goodiesCache.getBoosters(criteria=REQ_CRITERIA.BOOSTER.ACTIVE).values() if cmd.filter_types is None or booster.boosterType in cmd.filter_types
               ]