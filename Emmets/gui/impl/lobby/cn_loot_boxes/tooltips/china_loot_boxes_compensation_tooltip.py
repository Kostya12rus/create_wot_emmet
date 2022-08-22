# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/cn_loot_boxes/tooltips/china_loot_boxes_compensation_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.cn_loot_boxes.tooltips.china_loot_boxes_compensation_tooltip_model import ChinaLootBoxesCompensationTooltipModel, VehicleType
from gui.impl.pub import ViewImpl
from gui.shared.money import Currency
from shared_utils import first

class ChinaLootBoxesCompensationTooltip(ViewImpl):
    __slots__ = ('__data', )

    def __init__(self, compensationData):
        settings = ViewSettings(R.views.lobby.cn_loot_boxes.tooltips.ChinaLootBoxesCompensationTooltip())
        settings.model = ChinaLootBoxesCompensationTooltipModel()
        self.__data = compensationData
        super(ChinaLootBoxesCompensationTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ChinaLootBoxesCompensationTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as (model):
            model.setIconBefore(self.__data['iconBefore'])
            model.setVehicleLevel(self.__data['vehicleLevel'])
            model.setVehicleType(VehicleType(self.__data['vehicleType']))
            model.setVehicleName(self.__data['vehicleName'])
            model.setCompensationCurrency(self.__data['compensation'].get('currency', first(Currency.BY_WEIGHT)))
            model.setCompensationValue(self.__data['compensation'].get('value', 0))