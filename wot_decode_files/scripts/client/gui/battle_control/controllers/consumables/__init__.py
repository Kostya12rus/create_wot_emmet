# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/consumables/__init__.py
from constants import ARENA_BONUS_TYPE
from gui.battle_control.controllers.consumables import ammo_ctrl
from gui.battle_control.controllers.consumables import equipment_ctrl
from gui.battle_control.controllers.consumables import opt_devices_ctrl
from gui.battle_control.controllers.consumables import comp7_equipment_ctrl
from gui.battle_control.controllers.consumables import epic_equipment_ctrl
_EQUIPMENT_CONTROLLERS = {ARENA_BONUS_TYPE.COMP7: comp7_equipment_ctrl.Comp7EquipmentController, 
   ARENA_BONUS_TYPE.TOURNAMENT_COMP7: comp7_equipment_ctrl.Comp7EquipmentController, 
   ARENA_BONUS_TYPE.EPIC_BATTLE: epic_equipment_ctrl.EpicEquipmentsController}
_REPLAY_EQUIPMENT_CONTROLLERS = {ARENA_BONUS_TYPE.COMP7: comp7_equipment_ctrl.Comp7ReplayEquipmentController, 
   ARENA_BONUS_TYPE.EPIC_BATTLE: epic_equipment_ctrl.EpicReplayEquipmentController}

def createAmmoCtrl(setup):
    if setup.isReplayRecording:
        return ammo_ctrl.AmmoReplayRecorder(setup.replayCtrl)
    if setup.isReplayPlaying:
        return ammo_ctrl.AmmoReplayPlayer(setup.replayCtrl)
    return ammo_ctrl.AmmoController()


def createEquipmentCtrl(setup):
    if setup.isReplayPlaying:
        clazz = _REPLAY_EQUIPMENT_CONTROLLERS.get(setup.arenaEntity.bonusType, equipment_ctrl.EquipmentsReplayPlayer)
    else:
        clazz = _EQUIPMENT_CONTROLLERS.get(setup.arenaEntity.bonusType, equipment_ctrl.EquipmentsController)
    return clazz(setup)


def createOptDevicesCtrl(setup):
    return opt_devices_ctrl.OptionalDevicesController(setup)


__all__ = ('createAmmoCtrl', 'createEquipmentCtrl', 'createOptDevicesCtrl')