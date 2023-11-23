# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/comp7_slot_model.py
from gui.impl.gen.view_models.views.lobby.platoon.platoon_rank_data import PlatoonRankData
from gui.impl.gen.view_models.views.lobby.platoon.slot_model import SlotModel

class Comp7SlotModel(SlotModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(Comp7SlotModel, self).__init__(properties=properties, commands=commands)

    @property
    def rankData(self):
        return self._getViewModel(12)

    @staticmethod
    def getRankDataType():
        return PlatoonRankData

    def getIsWaiting(self):
        return self._getBool(13)

    def setIsWaiting(self, value):
        self._setBool(13, value)

    def _initialize(self):
        super(Comp7SlotModel, self)._initialize()
        self._addViewModelProperty('rankData', PlatoonRankData())
        self._addBoolProperty('isWaiting', False)