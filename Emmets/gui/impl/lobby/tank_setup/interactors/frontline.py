# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/interactors/frontline.py
from wg_async import wg_await, wg_async
from BWUtil import AsyncReturn
from adisp import adisp_process
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants
from gui.impl.lobby.tank_setup.interactors.base_equipment import BaseEquipmentInteractor
from gui.shared.event_dispatcher import showBattleAbilitiesConfirmDialog
from gui.shared.gui_items.items_actions import factory as ActionsFactory

class FrontlineInteractor(BaseEquipmentInteractor):
    __slots__ = ('_checkboxState', )

    def __init__(self, vehItem):
        super(FrontlineInteractor, self).__init__(vehItem)
        self._checkboxState = False

    def getName(self):
        return TankSetupConstants.BATTLE_ABILITIES

    def getInstalledLayout(self):
        return self.getItem().battleAbilities.installed

    def getCurrentLayout(self):
        return self.getItem().battleAbilities.layout

    def getSetupLayout(self):
        return self.getItem().battleAbilities.setupLayouts

    def revert(self):
        self.getItem().battleAbilities.setLayout(*self.getPlayerLayout())
        self._resetInstalledIndices()
        self.onSlotAction(actionType=BaseSetupModel.REVERT_SLOT_ACTION)
        self.itemUpdated()

    def updateFrom(self, vehicle, onlyInstalled=True):
        super(FrontlineInteractor, self).updateFrom(vehicle, onlyInstalled)
        items = self.getItem().battleAbilities
        items.setInstalled(*vehicle.battleAbilities.installed)
        items.setupLayouts.setSetups(vehicle.battleAbilities.setupLayouts.setups)
        self._playerLayout = vehicle.battleAbilities.layout.copy()
        if not onlyInstalled:
            self.getItem().battleAbilities.setLayout(*vehicle.battleAbilities.layout)

    @adisp_process
    def confirm(self, callback, skipDialog=False):
        action = ActionsFactory.getAction(ActionsFactory.INSTALL_BATTLE_ABILITIES, self.getItem(), self._checkboxState)
        if action is not None:
            result = yield action.doAction()
            callback(result)
        else:
            callback(None)
        return

    def setCheckboxState(self, state):
        self._checkboxState = state

    @wg_async
    def showExitConfirmDialog(self):
        vehicle = self.getItem()
        if not self._checkboxState:
            setupItems = self.getChangedList()
        else:
            setupItems = vehicle.battleAbilities.layout.getStorage
        result = yield wg_await(showBattleAbilitiesConfirmDialog(items=setupItems, withInstall=bool(setupItems), vehicleType=vehicle.type, applyForAllVehiclesByType=self._checkboxState))
        raise AsyncReturn(result)