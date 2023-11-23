# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/sub_views/halloween_setup.py
from gui.impl.lobby.tank_setup.sub_views.base_equipment_setup import BaseEquipmentSetupSubView
from gui.impl.lobby.tank_setup.configurations.halloween import HalloweenTabsController, HalloweenDealPanel

class HalloweenSetupSubView(BaseEquipmentSetupSubView):
    __slots__ = ()

    def revertItem(self, slotID):
        self._interactor.revertSlot(slotID)
        self.update()

    def _createTabsController(self):
        return HalloweenTabsController()

    def _getDealPanel(self):
        return HalloweenDealPanel