# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/vehicle_model_helpers.py
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.lobby.platoon.platoon_helpers import removeNationFromTechName
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.utils.functions import replaceHyphenToUnderscore

def fillVehicleModel(model, vehicleItem):
    model.setIsPremium(vehicleItem.isPremium or vehicleItem.isElite)
    model.setName(vehicleItem.shortUserName)
    model.setTechName(replaceHyphenToUnderscore(removeNationFromTechName(vehicleItem.name)))
    model.setTier(vehicleItem.level)
    model.setType(vehicleItem.type)
    model.setNation(vehicleItem.nationName)
    model.setVehicleCD(vehicleItem.compactDescr)