# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_reserves/reserves_conversion_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_reserves.converted_booster_list import ConvertedBoosterList

class ReservesConversionViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=4, commands=1):
        super(ReservesConversionViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def battleXPConverted(self):
        return self._getViewModel(0)

    @staticmethod
    def getBattleXPConvertedType():
        return ConvertedBoosterList

    @property
    def creditsConverted(self):
        return self._getViewModel(1)

    @staticmethod
    def getCreditsConvertedType():
        return ConvertedBoosterList

    @property
    def crewXPConverted(self):
        return self._getViewModel(2)

    @staticmethod
    def getCrewXPConvertedType():
        return ConvertedBoosterList

    @property
    def freeXPConverted(self):
        return self._getViewModel(3)

    @staticmethod
    def getFreeXPConvertedType():
        return ConvertedBoosterList

    def _initialize(self):
        super(ReservesConversionViewModel, self)._initialize()
        self._addViewModelProperty('battleXPConverted', ConvertedBoosterList())
        self._addViewModelProperty('creditsConverted', ConvertedBoosterList())
        self._addViewModelProperty('crewXPConverted', ConvertedBoosterList())
        self._addViewModelProperty('freeXPConverted', ConvertedBoosterList())
        self.onClose = self._addCommand('onClose')