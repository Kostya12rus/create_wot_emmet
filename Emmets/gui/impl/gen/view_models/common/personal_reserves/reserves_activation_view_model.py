# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/personal_reserves/reserves_activation_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.personal_reserves.reserves_group_model import ReservesGroupModel

class ReservesActivationViewModel(ViewModel):
    __slots__ = ('onInformationClicked', 'onNavigateToStore', 'onClose', 'onBoosterActivate')

    def __init__(self, properties=3, commands=4):
        super(ReservesActivationViewModel, self).__init__(properties=properties, commands=commands)

    def getReserveGroups(self):
        return self._getArray(0)

    def setReserveGroups(self, value):
        self._setArray(0, value)

    @staticmethod
    def getReserveGroupsType():
        return ReservesGroupModel

    def getGold(self):
        return self._getNumber(1)

    def setGold(self, value):
        self._setNumber(1, value)

    def getCanActivateClanReserves(self):
        return self._getBool(2)

    def setCanActivateClanReserves(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(ReservesActivationViewModel, self)._initialize()
        self._addArrayProperty('reserveGroups', Array())
        self._addNumberProperty('gold', 0)
        self._addBoolProperty('canActivateClanReserves', False)
        self.onInformationClicked = self._addCommand('onInformationClicked')
        self.onNavigateToStore = self._addCommand('onNavigateToStore')
        self.onClose = self._addCommand('onClose')
        self.onBoosterActivate = self._addCommand('onBoosterActivate')