# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/halloween/tooltips/characteristic_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.halloween.tooltips.characteristic_tooltip_model import CharacteristicTooltipModel, RoleEnum
from gui.impl.pub import ViewImpl

class CharacteristicTooltip(ViewImpl):
    __slots__ = ('__vehType', )

    def __init__(self, vehType):
        settings = ViewSettings(R.views.lobby.halloween.tooltips.CharacteristicTooltip())
        settings.model = CharacteristicTooltipModel()
        self.__vehType = vehType
        super(CharacteristicTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CharacteristicTooltip, self).getViewModel()

    def _onLoading(self):
        super(CharacteristicTooltip, self)._onLoading()
        settings = {'lightTank': RoleEnum.INITIATOR, 
           'mediumTank': RoleEnum.UNIVERSAL, 
           'heavyTank': RoleEnum.HELPER}
        role = settings[self.__vehType]
        self.viewModel.setRole(role)