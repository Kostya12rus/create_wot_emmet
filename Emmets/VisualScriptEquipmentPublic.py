# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/VisualScriptEquipmentPublic.py
from constants import EQUIPMENT_STAGES as STAGES
from VisualScriptEquipment import VisualScriptEquipment
from helpers.fixed_dict import getVisualScriptEquipmentPublicState

class VisualScriptEquipmentPublic(VisualScriptEquipment):

    def _onAvatarReady(self):
        super(VisualScriptEquipmentPublic, self)._onAvatarReady()
        self.set_equipmentStatePublic()

    def set_equipmentStatePublic(self, _=None):
        if self._context is None:
            return
        else:
            if not self.entity.isMyVehicle:
                state = getVisualScriptEquipmentPublicState(self.equipmentStatePublic)
                getattr(self._context, STAGES.toString(state.stage))()
            return