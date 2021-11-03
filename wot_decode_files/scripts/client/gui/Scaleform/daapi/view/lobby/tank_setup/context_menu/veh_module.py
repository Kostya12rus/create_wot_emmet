# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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