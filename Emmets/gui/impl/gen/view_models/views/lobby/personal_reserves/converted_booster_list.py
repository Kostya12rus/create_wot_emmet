# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_reserves/converted_booster_list.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_reserves.converted_booster_list_item import ConvertedBoosterListItem

class ConvertedBoosterList(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ConvertedBoosterList, self).__init__(properties=properties, commands=commands)

    def getOldBoosters(self):
        return self._getArray(0)

    def setOldBoosters(self, value):
        self._setArray(0, value)

    @staticmethod
    def getOldBoostersType():
        return ConvertedBoosterListItem

    def getNewBoosters(self):
        return self._getArray(1)

    def setNewBoosters(self, value):
        self._setArray(1, value)

    @staticmethod
    def getNewBoostersType():
        return ConvertedBoosterListItem

    def _initialize(self):
        super(ConvertedBoosterList, self)._initialize()
        self._addArrayProperty('oldBoosters', Array())
        self._addArrayProperty('newBoosters', Array())