# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/resource_well_requester.py
import typing, BigWorld
from adisp import adisp_async
from gui.resource_well.resource_well_constants import RESOURCE_WELL_PDATA_KEY
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IResourceWellRequester
if typing.TYPE_CHECKING:
    from typing import Dict

class ResourceWellRequester(AbstractSyncDataRequester, IResourceWellRequester):

    def getCurrentPoints(self):
        return self.getCacheValue('points', 0)

    def getBalance(self):
        return self.getCacheValue('balance', {})

    def getReward(self):
        return self.getCacheValue('reward', None)

    def getInitialNumberAmounts(self):
        return self.getCacheValue('initialAmounts', {})

    def _preprocessValidData(self, data):
        return dict(data.get(RESOURCE_WELL_PDATA_KEY, {}))

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().resourceWell.getCache((lambda resID, value: self._response(resID, value, callback)))