# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/vehicle_model_helpers.py
import typing
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.lobby.platoon.platoon_helpers import removeNationFromTechName
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.utils.functions import replaceHyphenToUnderscore
if typing.TYPE_CHECKING:
    from typing import Optional, Iterable

def fillVehicleModel(model, vehicleItem, tags=None):
    model.setIsPremium(vehicleItem.isPremium or vehicleItem.isElite)
    model.setName(vehicleItem.descriptor.type.shortUserString)
    model.setTechName(replaceHyphenToUnderscore(removeNationFromTechName(vehicleItem.name)))
    model.setTier(vehicleItem.level)
    model.setRoleKey(vehicleItem.roleLabel)
    model.setType(vehicleItem.type)
    model.setNation(vehicleItem.nationName)
    model.setVehicleCD(vehicleItem.compactDescr)
    if not tags:
        return
    model.setTags((',').join(frozenset(tags) & vehicleItem.tags))