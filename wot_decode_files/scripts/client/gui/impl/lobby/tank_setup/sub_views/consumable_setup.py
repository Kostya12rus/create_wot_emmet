# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/sub_views/consumable_setup.py
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabsController
from gui.impl.lobby.tank_setup.sub_views.base_equipment_setup import BaseEquipmentSetupSubView

class ConsumableSetupSubView(BaseEquipmentSetupSubView):
    __slots__ = ()

    def revertItem(self, slotID):
        self._interactor.revertSlot(slotID)
        self.update()

    def _createTabsController(self):
        return ConsumableTabsController()

    def _addListeners(self):
        super(ConsumableSetupSubView, self)._addListeners()
        self._addSlotAction(BaseSetupModel.ADD_ONE_SLOT_ACTION, self.__onAdd)

    def __onAdd(self, args):
        itemIntCD = int(args.get('intCD'))
        self._interactor.buyMore(itemIntCD)