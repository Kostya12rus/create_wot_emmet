# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/messengerBar/VehicleCompareCartButton.py
from gui.Scaleform.daapi.view.meta.ButtonWithCounterMeta import ButtonWithCounterMeta
from helpers import dependency
from skeletons.gui.game_control import IVehicleComparisonBasket

class VehicleCompareCartButton(ButtonWithCounterMeta):
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def _populate(self):
        super(VehicleCompareCartButton, self)._populate()
        self.comparisonBasket.onChange += self.__onCountChanged
        self.comparisonBasket.onSwitchChange += self.__onVehCmpBasketStateChanged
        self.__changeCount(self.comparisonBasket.getVehiclesCount())

    def _dispose(self):
        self.comparisonBasket.onChange -= self.__onCountChanged
        self.comparisonBasket.onSwitchChange -= self.__onVehCmpBasketStateChanged
        super(VehicleCompareCartButton, self)._dispose()

    def __onVehCmpBasketStateChanged(self):
        if not self.comparisonBasket.isEnabled():
            self.destroy()

    def __onCountChanged(self, _):
        self.__changeCount(self.comparisonBasket.getVehiclesCount())

    def __changeCount(self, count):
        self.as_setCountS(count)