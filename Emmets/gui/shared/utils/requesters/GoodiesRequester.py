# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/GoodiesRequester.py
from collections import namedtuple
import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IGoodiesRequester
GoodieVariable = namedtuple('GoodieVariable', 'state finishTime count')

class _ClanReserveInfo(namedtuple('_ClanReserveInfo', 'finishTime value duration')):
    __slots__ = ()

    def __new__(cls, finishTime, value, duration=3600):
        return super(_ClanReserveInfo, cls).__new__(cls, finishTime, value, duration)


class GoodiesRequester(AbstractSyncDataRequester, IGoodiesRequester):

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().goodies.getCache((lambda resID, value: self._response(resID, value, callback)))

    @property
    def goodies(self):
        return self.getCacheValue('goodies', {})

    @property
    def pr2ConversionResult(self):
        return self.getCacheValue('pr2_conversion', tuple())

    def getActiveClanReserves(self):
        return self.getCacheValue('clanReserves', {})

    def _preprocessValidData(self, data):
        data = dict(data)
        goodies = data.get('goodies', {})
        data['goodies'] = {gID: GoodieVariable(*data) for gID, data in goodies.iteritems()}
        clanReserves = {}
        for crID, crData in data.get('clanReserves', {}).iteritems():
            clanReserves[crID] = _ClanReserveInfo(crData['timeExpiration'], crData['factors'], crData['duration'])

        data['clanReserves'] = clanReserves
        return data