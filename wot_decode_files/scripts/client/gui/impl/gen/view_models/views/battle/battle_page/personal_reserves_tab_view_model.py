# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/personal_reserves_tab_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.personal_reserves.reserves_group_model import ReservesGroupModel

class PersonalReservesTabViewModel(ViewModel):
    __slots__ = ('onBoosterActivate', )

    def __init__(self, properties=1, commands=1):
        super(PersonalReservesTabViewModel, self).__init__(properties=properties, commands=commands)

    def getReserveGroups(self):
        return self._getArray(0)

    def setReserveGroups(self, value):
        self._setArray(0, value)

    @staticmethod
    def getReserveGroupsType():
        return ReservesGroupModel

    def _initialize(self):
        super(PersonalReservesTabViewModel, self)._initialize()
        self._addArrayProperty('reserveGroups', Array())
        self.onBoosterActivate = self._addCommand('onBoosterActivate')