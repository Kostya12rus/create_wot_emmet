# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/sub_views/battle_booster_setup.py
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.lobby.tank_setup.configurations.battle_booster import BattleBoostersTabsController, BattleBoosterTabs
from gui.impl.lobby.tank_setup.sub_views.base_equipment_setup import BaseEquipmentSetupSubView

class BattleBoosterSetupSubView(BaseEquipmentSetupSubView):
    __slots__ = ()

    def updateSlots(self, slotID, fullUpdate=True, updateData=True):
        item = self._interactor.getCurrentLayout()[slotID]
        if item is not None:
            self._setTab(BattleBoosterTabs.CREW if item.isCrewBooster() else BattleBoosterTabs.OPT_DEVICE)
        if item is not None and item.isHidden and not item.isInInventory:
            self._interactor.changeSlotItem(slotID, None)
            self._interactor.getAutoRenewal().setLocalValue(False)
        super(BattleBoosterSetupSubView, self).updateSlots(slotID, fullUpdate, updateData)
        return

    def revertItem(self, slotID):
        self._interactor.revertSlot(slotID)
        self.update()

    def _createTabsController(self):
        return BattleBoostersTabsController()

    def _addListeners(self):
        super(BattleBoosterSetupSubView, self)._addListeners()
        self._addSlotAction(BaseSetupModel.ADD_ONE_SLOT_ACTION, self.__onAdd)

    def __onAdd(self, args):
        itemIntCD = int(args.get('intCD'))
        self._interactor.buyMore(itemIntCD)