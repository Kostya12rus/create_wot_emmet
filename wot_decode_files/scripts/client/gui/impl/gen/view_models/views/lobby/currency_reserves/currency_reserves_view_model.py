# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/currency_reserves/currency_reserves_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.currency_reserves.currency_reserve_model import CurrencyReserveModel

class CurrencyReservesViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=3, commands=1):
        super(CurrencyReservesViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def creditReserve(self):
        return self._getViewModel(0)

    @staticmethod
    def getCreditReserveType():
        return CurrencyReserveModel

    @property
    def goldReserve(self):
        return self._getViewModel(1)

    @staticmethod
    def getGoldReserveType():
        return CurrencyReserveModel

    def getTimeToOpen(self):
        return self._getNumber(2)

    def setTimeToOpen(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(CurrencyReservesViewModel, self)._initialize()
        self._addViewModelProperty('creditReserve', CurrencyReserveModel())
        self._addViewModelProperty('goldReserve', CurrencyReserveModel())
        self._addNumberProperty('timeToOpen', 0)
        self.onClose = self._addCommand('onClose')