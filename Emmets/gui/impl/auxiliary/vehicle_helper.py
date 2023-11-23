# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/auxiliary/vehicle_helper.py
import typing
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS
if typing.TYPE_CHECKING:
    from typing import Optional, Iterable
    from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
    from gui.shared.gui_items.Vehicle import Vehicle

def fillVehicleInfo(vehInfo, vehicle, separateIGRTag=False, tags=None):
    isElite = not vehicle.getEliteStatusProgress().toUnlock or vehicle.isElite
    vehInfo.setIsElite(isElite)
    vehInfo.setVehicleLvl(vehicle.level)
    vehInfo.setVehicleType(vehicle.type)
    vehInfo.setVehicleNation(vehicle.nationName)
    vehInfo.setVehicleShortName(vehicle.descriptor.type.shortUserString)
    vehicleTags = set(tags or [])
    vehicleTags.add(VEHICLE_TAGS.PREMIUM_IGR)
    vehInfo.setTags((',').join(vehicleTags & vehicle.tags))
    if separateIGRTag:
        vehInfo.setVehicleName(vehicle.descriptor.type.userString)
    else:
        vehInfo.setVehicleName(vehicle.descriptor.type.shortUserString)