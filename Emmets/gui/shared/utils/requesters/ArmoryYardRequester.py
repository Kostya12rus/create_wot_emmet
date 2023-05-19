# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/ArmoryYardRequester.py
import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IArmoryYardRequester

class ArmoryYardRequester(AbstractSyncDataRequester, IArmoryYardRequester):

    @property
    def data(self):
        return self._data

    @property
    def progressionLevel(self):
        from armory_yard_constants import PROGRESSION_LEVEL_PDATA_KEY
        return self._data.get(PROGRESSION_LEVEL_PDATA_KEY, 0)

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().armoryYard.getCache((lambda resID, value: self._response(resID, value, callback)))

    def _preprocessValidData(self, data):
        from armory_yard_constants import PDATA_KEY_ARMORY_YARD
        if PDATA_KEY_ARMORY_YARD in data:
            return dict(data[PDATA_KEY_ARMORY_YARD])
        return dict()