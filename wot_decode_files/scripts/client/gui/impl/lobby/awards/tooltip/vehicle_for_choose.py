# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/awards/tooltip/vehicle_for_choose.py
import typing
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.pub import ViewImpl
from frameworks.wulf import Array
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.awards.tooltips import awards_vehicle_for_choose_tooltip_view_model as a

class VehicleForChooseTooltipContent(ViewImpl):
    __slots__ = ()

    @property
    def viewModel(self):
        return super(VehicleForChooseTooltipContent, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(VehicleForChooseTooltipContent, self)._initialize(*args, **kwargs)
        with self.viewModel.transaction() as (tx):
            vList = Array()
            for vehData in kwargs.get('vehicles', []):
                vR = VehicleInfoModel()
                vR.setIsElite(vehData.get('isElite', False))
                vR.setVehicleName(vehData.get('vehicleName', ''))
                vR.setVehicleType(vehData.get('vehicleType', ''))
                vR.setVehicleLvl(vehData.get('vehicleLvlNum', 1))
                vList.addViewModel(vR)

            tx.setVehiclesList(vList)