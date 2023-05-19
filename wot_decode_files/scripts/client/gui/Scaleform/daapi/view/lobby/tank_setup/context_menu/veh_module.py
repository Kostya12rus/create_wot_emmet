# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/context_menu/veh_module.py
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import CMLabel, option
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base import BaseItemContextMenu, TankSetupCMLabel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from ids_generators import SequenceIDGenerator

class VehModuleItemContextMenu(BaseItemContextMenu):
    __sqGen = SequenceIDGenerator()

    @option(__sqGen.next(), CMLabel.INFORMATION)
    def showInfo(self):
        self._sendSlotAction(BaseSetupModel.SHOW_INFO_SLOT_ACTION)

    @option(__sqGen.next(), TankSetupCMLabel.SELECT)
    def select(self):
        self._sendSlotAction(BaseSetupModel.SELECT_SLOT_ACTION)